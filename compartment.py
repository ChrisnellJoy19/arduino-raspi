from machine import Machine

class Compartment:
    def __init__(self, machine: Machine, commands: dict) -> None:
        """
        Initialize a new compartment object

        :param machine: Machine instance
        :param commands: List of commands to use in arduino
        
        .. code-block:: python
        commands = {
            'turn_off_relay': 0,
            'turn_on_relay': 1,
            'set_color_red': 2,
            'set_color_green': 3,
            'item_detection': 4,
            'turn_off_LED': 5,
        }
        """
        self.machine = machine
        self.turn_off_relay_cmd = commands.pop('turn_off_relay')
        self.turn_on_relay_cmd = commands.pop('turn_on_relay')
        self.set_color_red_cmd = commands.pop('set_color_red')
        self.set_color_green_cmd = commands.pop('set_color_green')
        self.item_detection_cmd = commands.pop('item_detection')
        self.turn_off_LED_cmd = commands.pop('turn_off_LED')

    def turn_off_relay(self):
        """
        Turn off relay
        """
        self.machine.send_command(self.turn_off_relay_cmd)
            
    def turn_on_relay(self):
        """
        Turn on relay
        """
        self.machine.send_command(self.turn_on_relay_cmd)

    def set_color_red(self):
        """
        Set LED to red
        """
        self.machine.send_command(self.set_color_red_cmd)

    def set_color_green(self):
        """
        Set LED to green
        """
        self.machine.send_command(self.set_color_green_cmd)

    def item_detection(self):
        """
        Detect item using ir proximity sensor
        """
        self.machine.send_command(self.item_detection_cmd)
        response = self.machine.get_arduino_response()
        while not response:
            response = self.machine.get_arduino_response()
        return response
    
    def turn_off_LED(self):
        """
        Turn off red and green LED
        """
        self.machine.send_command(self.turn_off_LED_cmd)