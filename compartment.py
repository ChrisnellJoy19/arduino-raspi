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
            'get_distance': 4 
        }
        """
        self.machine = machine
        self.turn_off_relay_cmd = commands.pop('turn_off_relay')
        self.turn_on_relay_cmd = commands.pop('turn_on_relay')
        self.set_color_red_cmd = commands.pop('set_color_red')
        self.set_color_green_cmd = commands.pop('set_color_green')
        self.set_color_blue_cmd = commands.pop('set_color_blue')
        self.get_distance_cmd = commands.pop('get_distance')

    def turn_off_relay(self):
        """
        Turn off relay
        """
        self.machine.send_command(self.turn_off_relay_cmd)
            
    def turn_on_relay(self):
            """
            lock
            """
            self.machine.send_command(self.turn_on_relay_cmd)

    def set_color_red(self):
            """
            set LED to red
            """
            self.machine.send_command(self.set_color_red_cmd)

    def set_color_green(self):
            """
            set LED to green
            """
            self.machine.send_command(self.set_color_green_cmd)

    def get_distance(self):
            """
            get distance
            """
            self.machine.send_command(self.get_distance_cmd)
            response = self.machine.get_arduino_response()
            while not response:
                response = self.machine.get_arduino_response()
            distance = float(response)
            return distance
