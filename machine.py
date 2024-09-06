#library
import serial

class Machine:
    def __init__(self) -> None: #initializer    
        self.available_commands = [0,1,2,3,4] 
        self.arduino = serial.Serial('COM9', 9600, timeout = 100) #represent arduino object

    def send_command(self, command: int):
        '''
        Send command to arduino. 
        Can be used to explicitly invoke Arduino operation without calling specific functions \n

        Parameters:
        command (int) : Command to send
        '''
        if(command in self.available_commands):
            while True:
                self.arduino.write(bytes(str(command)+'\n','utf-8'))
                response = self.get_arduino_response()
                if(response == 'ok'):
                    break
        else:
            raise Exception('Unknown command')



    def get_arduino_response(self) -> str:
        '''
        Get arduino serial response

        Returns:
        response (str) : Arduino response
        '''
        try:
            response = self.arduino.readline().decode('utf-8').rstrip()
        except UnicodeDecodeError:
            response = self.arduino.readline().decode('utf-8').rstrip()
        return response
    
    def turnOffRelay(self):
            '''
            unlock
            '''
            self.send_command(0)
            
    def turnOnRelay(self):
            '''
            lock
            '''
            self.send_command(1)

    def setColorRed(self):
            '''
            set LED to red
            '''
            self.send_command(2)

    def setColorGreen(self):
            '''
            set LED to green
            '''
            self.send_command(3)

    def getDistance(self):
            '''
            get distance
            '''
            self.send_command(4)
            response = self.get_arduino_response()
            print(response)
            while not response:
                response = self.get_arduino_response()
                print(response)
            distance = float(response)
            return distance
