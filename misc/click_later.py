import time
import os
import sys
from pynput.mouse import Button, Controller

from notes_exporter.src.notes_exporter import START_DELAY

START_DELAY = 3

mouse = Controller()

if len(sys.argv) < 2:
    SLEEP_DUR = 1
else:
    SLEEP_DUR = int(sys.argv[1])

time.sleep(START_DELAY)
# Read pointer position
print(f'The current pointer position is {mouse.position}')
# Save pointer position
mouse_pos = mouse.position

print(f'Clicking in: {SLEEP_DUR} seconds!')
time.sleep(SLEEP_DUR)

mouse.position = mouse_pos
mouse.click(Button.left, 1)
