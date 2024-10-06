import firebase_admin
import json
import random
import serial
import sys
import time 

from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from loguru import logger
from utils import (
    Compartment, 
    CompartmentStatus, 
    Transaction, 
    TransactionStatus,
    dateutil
)
from sim808 import Sim808

log_base_format = '<green>{time}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> | <level>{message}</level> {extra}\n'

def format_extra(extra):
    extra_str = ''
    if isinstance(extra, dict):
        extra_str = ' '.join(f'{key}={value}' for key, value in extra.items())
    elif isinstance(extra, str):
        extra_str = extra
    return extra_str

def log_format(record):
    record['extra'] = format_extra(record.get('extra', {}))
    return log_base_format.format(**record)

class Machine:
    def __init__(self, port: str = None, gsm_port: str = None, debug: bool = False) -> None:

        import compartment
        self.debug = debug
        self.logger = logger.bind()
        logger.remove()
        self.logger.add(
            f'logs/machine.log', 
            level="INFO", 
            format=log_format
        )
        logger.add(
            sys.stdout, 
            format=log_format,
            colorize=True
        )

        self.logger.info('Intializing machine')
        self.available_commands = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] 
        self.arduino = serial.Serial(port, 9600, timeout = 9) 
        if port:
            self.arduino.reset_input_buffer()
            self.arduino.reset_output_buffer()
        self.logger.info(f'Arduino initialized', port=port)


        cred = credentials.Certificate('service.json') 
        firebase_admin.initialize_app(cred)
        self.database = firestore.client()
        self.logger.info(f'Firestore initialized')

        # if not debug:
        #     self.sim808 = Sim808(gsm_port)
        # self.logger.info(f'Sim808 initialized')

        self.compartments: dict[str, compartment.Compartment] = {
            '1': compartment.Compartment(
                machine=self,
                commands = {
                    'turn_off_relay': 0,
                    'turn_on_relay': 1,
                    'set_color_red': 2,
                    'set_color_green': 3,
                    'item_detection': 4 
                }
            ),
            '2': compartment.Compartment(
                machine=self,
                commands = {
                    'turn_off_relay': 5,
                    'turn_on_relay': 6,
                    'set_color_red': 7,
                    'set_color_green': 8,
                    'item_detection': 9 
                }
            ),
            '3': compartment.Compartment(
                machine=self,
                commands = {
                    'turn_off_relay': 10,
                    'turn_on_relay': 11,
                    'set_color_red': 12,
                    'set_color_green': 13,
                    'item_detection': 14 
                }
            ),
        }
        self.logger.info(f'Compartments initialized')

    def send_command(self, command: int):
        """
        Send command to arduino. 
        Can be used to explicitly invoke Arduino operation without calling specific functions \n

        Parameters:
        command (int) : Command to send
        """
        self.logger.debug(f'Send Command to Arduino: {command}')
        if(command in self.available_commands):
            while True:
                self.arduino.write(bytes(str(command)+'\n','utf-8'))
                time.sleep(0.5)
                response = self.get_arduino_response()
                if(response == 'ok'):
                    break
        else:
            raise Exception('Unknown command')

    def get_arduino_response(self) -> str:
        """
        Get arduino serial response

        Returns:
        response (str) : Arduino response
        """
        try:
            response = self.arduino.readline().decode('utf-8').rstrip()
        except UnicodeDecodeError:
            response = self.arduino.readline().decode('utf-8').rstrip()
        self.logger.debug(f'Got response from arduino: {response}')
        return response

    def send_message(self, to: str, msg: str):
        """
        Send a message using twilio service. Phone or msg_service must be given

        :param to: Phone number to send to
        :param msg: Message body
        """
        if not self.debug:
            self.sim808.send_sms(to, msg)
        self.logger.info(f'Sent message to {to}')
        self.logger.info(f'Message: {msg}')

    def _generate_otp(self) -> str:
        """
        Generate random 4 digit OTP
        """
        otp = random.randint(1000, 9999)
        return str(otp)

    def validate_otp(self, compartment_id: str, otp: str) -> bool:
        """
        Validate if otp is valid for a compartment.
        OTP is validated against compartment's pending transaction

        :param compartment_id: Compartment number (must be a key of `self.compartments`)
        :param otp: One time password
        :return: Valid
        """
        transaction_collection = self.database.collection('transactions')

        pending_transaction = transaction_collection \
            .where(filter=FieldFilter('compartment_id', '==', compartment_id)) \
            .where(filter=FieldFilter('status', '==', TransactionStatus.pending)) \
            .limit(1) \
            .get()
        
        if not pending_transaction:
            return False
        
        pending_transaction = pending_transaction[0]
        transaction = Transaction(**pending_transaction.to_dict())

        if otp != transaction.otp:
            return False
        
        return True

    def get_compartment_status(self, compartment_id: str) -> str:
        """
        Get currnt status of given comparment ID

        :param compartment_id: Compartment number (must be a key of `self.compartments`)
        :return: Compartment status
        """
        compartment_document = self.database.collection('compartments').document(compartment_id)
        compartment = compartment_document.get()
        if not compartment.exists:
            self.logger.warning(f'Compartment {compartment_id} does not exists')
            raise Exception(f'Compartment {compartment_id} does not exists')
        
        compartment = Compartment(**compartment.to_dict())
        return compartment.status

    def dropoff_item(self, compartment_id: str, details: dict) -> str:
        """
        Emulate a drop-off operation on specific compartment

        :param compartment_id: Compartment number (must be a key of `self.compartments`)
        :param details: Drop-off detail, see `utils.Transaction` for details
        :return: Transaction otp
        """
        compartment_document = self.database.collection('compartments').document(compartment_id)
        transaction_collection = self.database.collection('transactions')
        #transaction_collection = self.database.orderBy("", "asc")

        datetime_now = dateutil.get_datetime_gmt()

        compartment = compartment_document.get()
        if not compartment.exists:
            self.logger.warning(f'Compartment {compartment_id} does not exists')
            raise Exception(f'Compartment {compartment_id} does not exists')
        
        # Get compartment status
        compartment = Compartment(**compartment.to_dict())
        if compartment.status != CompartmentStatus.available:
            self.logger.warning(f'Compartment {compartment_id} is not available', status=compartment.status)
            raise Exception(f'Compartment {compartment_id} is not available')
        
        # Get pending transaction
        pending_transaction = transaction_collection \
            .where(filter=FieldFilter('compartment_id', '==', compartment_id)) \
            .where(filter=FieldFilter('status', '==', TransactionStatus.pending)) \
            .limit(1) \
            .get()
        
        if pending_transaction:
            self.logger.warning(f'Compartment {compartment_id} has pending transaction')
            raise Exception(f'Compartment {compartment_id} has pending transaction')
        
        otp = self._generate_otp()
        transaction = Transaction(
            compartment_id=compartment.id, 
            status=TransactionStatus.pending, 
            otp=otp,
            dropoff_at=datetime_now,
            **details
        )
        _, transaction_ref = transaction_collection.add(transaction.model_dump())
        self.logger.info(f'Transaction added with id: {transaction_ref.id}')

        compartment.status = CompartmentStatus.unavailable
        compartment.updated_at = datetime_now
        compartment_document.set(compartment.model_dump(), merge=True)
        self.logger.info(f'Compartment updated with id: {compartment_id}')

        # Send message notification to sender and receiver contact

        return otp
    
    def release_item(self, compartment_id: str, otp: str) -> bool:
        """
        Emulate a release-off operation on specific compartment

        :param compartment_id: Compartment number (must be a key of `self.compartments`)
        :param otp: One time password
        :return: Release success
        """
        compartment_document = self.database.collection('compartments').document(compartment_id)
        transaction_collection = self.database.collection('transactions')
        datetime_now = dateutil.get_datetime_gmt()

        compartment = compartment_document.get()
        if not compartment.exists:
            self.logger.warning(f'Compartment {compartment_id} does not exists')
            raise Exception(f'Compartment {compartment_id} does not exists')
        
        # Get compartment status
        compartment = Compartment(**compartment.to_dict())
        if compartment.status != CompartmentStatus.unavailable:
            self.logger.warning(f'Compartment {compartment_id} is not unavailable', status=compartment.status)
            raise Exception(f'Compartment {compartment_id} is not unavailable')

        # Get pending transaction
        pending_transaction = transaction_collection \
            .where(filter=FieldFilter('compartment_id', '==', compartment_id)) \
            .where(filter=FieldFilter('status', '==', TransactionStatus.pending)) \
            .limit(1) \
            .get()
        
        if not pending_transaction:
            self.logger.warning(f'Compartment {compartment_id} has no pending transaction')
            raise Exception(f'Compartment {compartment_id} has no pending transaction')
        
        pending_transaction = pending_transaction[0]
        transaction = Transaction(**pending_transaction.to_dict())

        if otp != transaction.otp:
            self.logger.warning('OTP does not match')
            raise Exception('OTP does not match')
        
        transaction.received_at = datetime_now
        transaction.status = TransactionStatus.completed
        transaction_collection.document(pending_transaction.id).set(transaction.model_dump())
        self.logger.info(f'Transaction updated with id: {pending_transaction.id}')

        compartment.status = CompartmentStatus.available
        compartment.updated_at = datetime_now
        compartment_document.set(compartment.model_dump(), merge=True)
        self.logger.info(f'Compartment updated with id: {compartment_id}')

        # Send message notification to sender and receiver contact

        return True
