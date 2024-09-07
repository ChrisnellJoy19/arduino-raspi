from machine import Machine
from compartment import Compartment
import time

"""
Sample usage
"""

machine = Machine()

compartment1 = Compartment(
    machine=machine,
    commands = {
        'turn_off_relay': 0,
        'turn_on_relay': 1,
        'set_color_red': 2,
        'set_color_green': 3,
        'get_distance': 4 
    }
)


