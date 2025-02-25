import serial
import time
import datetime
import re

class Sim808:
    '''
    Initialize a Sim808 object for communicating with a SIM808 module

    Parameters:
    port (str) : Serial port of SIM808 module 
    '''
 
    def __init__(self, port):
        '''
        Initialize a Sim808 object for communicating with a SIM808 module

        Parameters:
        port (str) : Serial port of SIM808 module 
        '''
       
        self.sim808 = serial.Serial(port, 115200, timeout=5)
        self.initialize()

    def initialize(self):
        '''
        Check if SIM808 exists and functioning
        '''
        self.sim808.reset_input_buffer()
        self.sim808.reset_output_buffer()
        self.send_command('AT\r\n')
        response = self.read_response()
        time.sleep(5)
        print(response)
        if('OK' not in response):
            raise Exception('Error starting sim808')
        self.send_command('AT+CMGF=1\r\n')
        self.read_response()
 
    def read_response(self):
        '''
        Get the response from SIM808 Serial COM

        Returns:
        str : SIM808 response
        '''
        response = b''
        while(self.sim808.inWaiting()):
            bit = self.sim808.read()
            response += bit
        
        # Try decoding with UTF-8, ignoring errors for non-decodable bytes
        try:
            return response.decode('utf-8')
        except UnicodeDecodeError:
            return response.decode('utf-8', errors='ignore')  # Skip invalid characters

    def send_command(self, command: str, timeout: float = 1):
        '''
        Send a command to SIM808 Serial COM

        Parameters:
        command (str) : Command to send
        timeout (float) : Timeout allows module to receive command in full
        '''
        self.sim808.write(command.encode())
        time.sleep(timeout)
 
    def send_sms(self, number: str, message: str):
        '''
        Send a SMS message

        Parameters:
        number (str) : Number to send message to. Should contain country code
        message (str) : Message to send
        '''
        self.send_command('AT+CMGS="' + number + '"\r')
        time.sleep(0.1)
        self.send_command(message + '\x1A\n')
        print(f'Sleeping for {0.1*(len(message)/5)}s')
        time.sleep(0.1*(len(message)/5))
        response = self.read_response()
        while 'OK' not in response:
            time.sleep(0.1)
            response = self.read_response()
        print(response)

    def read_unread_sms(self):
        '''
        Get unread sms

        Returns:
        sms (str): unread sms
        '''
        self.send_command('AT+CMGL=\"REC UNREAD\"\r\n')
        time.sleep(1)
        response = self.read_response()
        return response

    def get_time(self):
        '''
        Get network date and time

        Returns:
        datetime (str) : Network date and time
        '''
        self.send_sms("+639155882825", "CLOCK COMMAND")
        start_time = datetime.datetime.now()
        time.sleep(3)
        messages = self.read_unread_sms()
        end_time = datetime.datetime.now()
        datetime_pattern = r'\d{2}/\d{2}/\d{2},\d{2}:\d{2}:\d{2}\+32'
        match = re.findall(datetime_pattern, messages)
        if match:
            returned_datetime = datetime.datetime.strptime(match[-1].replace('+32',''),'%y/%m/%d,%H:%M:%S')
            returned_datetime += (end_time - start_time)
        return returned_datetime
    
    def delete_all_sms(self):
        '''
        Delete all stored sms (inbox and sent)
        '''
        self.send_command('AT+CMGD=1,4\r\n')
        time.sleep(5)
