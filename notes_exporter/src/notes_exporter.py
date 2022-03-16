import time
import os
import sys
import pyperclip
from pynput import mouse, keyboard

# Set delay between program start and first automatic action
if len(sys.argv) < 2:
    START_DELAY = 1
else:
    START_DELAY = int(sys.argv[1])

# Delay between keyboard/mouse inputs
INPUT_DELAY = 1


# Press and release cmd+a
def select_all_text(my_keyboard):
    my_keyboard.press(keyboard.Key.cmd)
    my_keyboard.press('a')
    my_keyboard.release(keyboard.Key.cmd)
    my_keyboard.release('a')

# Press and release cmd+c
def copy_text(my_keyboard):
    my_keyboard.press(keyboard.Key.cmd)
    my_keyboard.press('c')
    my_keyboard.release(keyboard.Key.cmd)
    my_keyboard.release('c')

# Create /notes dir to save each note txt file
def create_notes_dir():
    try:
        if 'notes' not in os.listdir('.'):
            os.mkdir('notes')
    except OSError as e:
        print(f'Attempted to create notes dir that already exists: {e}')

def save_cur_note(my_mouse, my_keyboard):
    # Click on notes window to focus it
    my_mouse.click(mouse.Button.left, 2)
    time.sleep(INPUT_DELAY)

    # Select all text in the notes window and copy it to keyboard
    select_all_text(my_keyboard)
    time.sleep(INPUT_DELAY)
    copy_text(my_keyboard)

    # Extract notes text from clipboard and separate to header, body
    text = pyperclip.paste()
    text_lines = text.split("\n")
    header = text_lines[0].rstrip()
    body = '\n'.join(text_lines[1:])

    # Log processed text
    print(header)
    print(body)

    # Create notes dir if not exists and write a text file for the current note
    create_notes_dir()
    with open(f'notes/{header}.txt', 'w') as f:
        f.write(body)


def main():
    # init mouse and keyboard controllers
    my_mouse = mouse.Controller()
    my_keyboard = keyboard.Controller()

    # Save pointer position
    notes_pos = my_mouse.position
    print(f'The Notes pointer position is {notes_pos}')
    print(f'Clicking in: {START_DELAY} seconds!')
    time.sleep(START_DELAY)

    save_cur_note(my_mouse, my_keyboard)

    # Reset cursor to notes_pos

    # Enter shortcut keys to move down to next note

    # Run save_cur_note

    # TODO: When does the loop stop?
    # Detect if notes/{header}.txt is already in the dir, if so then quit


if __name__ == '__main__':
    main()