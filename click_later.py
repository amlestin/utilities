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
#TODO: Save current pointer position for use after delay

print(f'Clicking in: {delay} seconds!')
time.sleep(delay)

mouse.click(Button.left, 1)
