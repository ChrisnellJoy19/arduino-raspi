#main logic of the machine
import time
from machine import Machine

machine = Machine()
# machine.send_command(3)
machine.getDistance()
distance = machine.getDistance()
print(distance)






