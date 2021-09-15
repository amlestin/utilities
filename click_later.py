import time
from pynput.mouse import Button, Controller

mouse = Controller()

delay = 1

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

time.sleep(delay)
mouse.click(Button.left, 1)