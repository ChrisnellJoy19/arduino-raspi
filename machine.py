import serial

class Machine:
    def __init__(self) -> None: 
        self.available_commands = [0,1,2,3,4] 
        self.arduino = serial.Serial('COM9', 9600, timeout = 1) 

    def send_command(self, command: int):
        """
        Send command to arduino. 
        Can be used to explicitly invoke Arduino operation without calling specific functions \n

        Parameters:
        command (int) : Command to send
        """
        if(command in self.available_commands):
            while True:
                self.arduino.write(bytes(str(command)+'\n','utf-8'))
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
        return response
