from asyncore import write
import time
import os
import sys
from pynput import mouse, keyboard
import pyperclip

my_mouse = mouse.Controller()
my_keyboard = keyboard.Controller()

if len(sys.argv) < 2:
    delay = 1
else:
    delay = int(sys.argv[1])

# Read pointer position
print(f'The Notes pointer position is {my_mouse.position}')
#TODO: Save current pointer position for use after delay

print(f'Clicking in: {delay} seconds!')
time.sleep(delay)

my_mouse.click(mouse.Button.left, 1)
time.sleep(1)
my_mouse.click(mouse.Button.left, 1)


# Press and release cmd+a
my_keyboard.press(keyboard.Key.cmd)
my_keyboard.press('a')
my_keyboard.release(keyboard.Key.cmd)
my_keyboard.release('a')
time.sleep(1)

# Press and release cmd+c
my_keyboard.press(keyboard.Key.cmd)
my_keyboard.press('c')
my_keyboard.release(keyboard.Key.cmd)
my_keyboard.release('c')

text = pyperclip.paste()

text_lines = text.split("\n")
header = text_lines[0].rstrip()
body = '\n'.join(text_lines[1:])

print(header)
print(body)

try:
    os.mkdir('notes')
except OSError as e:
    print(f'notes dir exists: {e}')

with open(f'notes/{header}.txt', 'w') as f:
    f.write(body)
