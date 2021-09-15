import time
import os
import sys
from pynput.mouse import Button, Controller

mouse = Controller()

if len(sys.argv) < 2:
    delay = 1
else:
    delay = int(sys.argv[1])

# Read pointer position
print(f'The current pointer position is {mouse.position}')

time.sleep(delay)
mouse.click(Button.left, 1)