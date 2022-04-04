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

# Create hash of file
# Python program to find the SHA-1 message digest of a file
# https://www.programiz.com/python-programming/examples/hash-file
# importing the hashlib module
import hashlib

def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename,'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()

# Press and release ESC
def press_esc(my_keyboard):
    my_keyboard.press(keyboard.Key.esc)
    my_keyboard.release(keyboard.Key.esc)

# Press and release right arrow key
def press_right_arrow(my_keyboard):
    my_keyboard.press(keyboard.Key.right)
    my_keyboard.release(keyboard.Key.right)

# Press and release left arrow key
def press_left_arrow(my_keyboard):
    my_keyboard.press(keyboard.Key.left)
    my_keyboard.release(keyboard.Key.left)

# Press and release down arrow key
def press_down_arrow(my_keyboard):
    my_keyboard.press(keyboard.Key.down)
    my_keyboard.release(keyboard.Key.down)

# Press cmd+2 to activate gallery view
def press_cmd_2(my_keyboard):
    my_keyboard.press(keyboard.Key.cmd)
    my_keyboard.press('2')
    my_keyboard.release(keyboard.Key.cmd)
    my_keyboard.release('2')


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
    if text is None:
        time.sleep(INPUT_DELAY)
        text = pyperclip.paste()

    try:
        text_lines = text.split("\n")
        header = text_lines[0].rstrip()
        body = '\n'.join(text_lines[1:])
    except Exception as e:
        print("Error: could not paste text: {e}")

    # Log processed text
    print(header)
    print(body)

    # Create notes dir if not exists
    try:
        create_notes_dir()
    except OSError as e:
            print("Failed to create a notes directory")
            return -1

    # Write a text file for the current note
    try:
        filename = f'notes/{header}.txt'
        with open(filename, 'w') as f:
            f.write(body)
            return hash_file(filename)
    except Exception as e:
        print(f"Failed to write the note file due to {e}")
        return -1

def main():
    # init mouse and keyboard controllers
    my_mouse = mouse.Controller()
    my_keyboard = keyboard.Controller()

    # Save pointer position
    notes_pos = my_mouse.position
    print(f'The Notes pointer position is {notes_pos}')
    print(f'Clicking in: {START_DELAY} seconds!')
    time.sleep(START_DELAY)

    press_cmd_2(my_keyboard=my_keyboard)
    
    created_file = save_cur_note(my_mouse, my_keyboard)

    # Reset cursor to notes_pos
    my_mouse.position = notes_pos

    # Enter shortcut keys to move down to next note
    # Found the shortcuts: https://support.apple.com/guide/notes/keyboard-shortcuts-and-gestures-apd46c25187e/mac
    # TODO: Implement the loop using the gallery view shortcut CMD+2, Enter to read a note, copy, then ESC
    # right arrow for next note until the same note repeats (end of row), then backtrack to beginning or row, hit down arrow


    # Run save_cur_note until end of notes
    # Detects if the sha1 hash of notes/{header}.txt is already in the dir, if so then quit
    last_created_file = ''
    while True:
        created_file = save_cur_note(my_mouse, my_keyboard)
        if created_file == last_created_file:
            print("A file was written twice. End of notes reached.")
            break
        else:
            last_created_file = created_file
        press_esc(my_keyboard=my_keyboard)


if __name__ == '__main__':
    main()