import time
import os
import sys
import pyperclip
import hashlib
import re
import logging
import keyboard_helpers as kh
from pynput import mouse, keyboard

logging.basicConfig()
logger = logging.getLogger("notes-exporter")
logger.setLevel(logging.INFO)

# Set delay between program start and first automatic action
if len(sys.argv) < 2:
    START_DELAY = 1
else:
    START_DELAY = int(sys.argv[1])

# Delay between keyboard/mouse inputs
INPUT_DELAY = 1

# Create /notes dir to save each note txt file
def create_notes_dir():
    try:
        if 'notes' not in os.listdir('.'):
            os.mkdir('notes')
    except OSError as e:
        logger.info(f'Attempted to create notes dir that already exists: {e}')


def save_cur_note(my_mouse, my_keyboard):
    # Select all text in the notes window and copy it to keyboard
    kh.select_all_text(my_keyboard)
    time.sleep(INPUT_DELAY)
    kh.copy_text(my_keyboard)

    # Extract notes text from clipboard and separate to header, body
    text = pyperclip.paste()
    if text is None:
        time.sleep(INPUT_DELAY)
        text = pyperclip.paste()
        pyperclip.copy('')

    try:
        text_lines = text.split("\n")
        header = text_lines[0].rstrip()
        body = '\n'.join(text_lines[1:])
    except Exception as e:
        logger.info("Error: could not paste text: {e}")

    # Create notes dir if not exists
    try:
        create_notes_dir()
    except OSError as e:
            logger.info("Failed to create a notes directory")
            return -1

    # Write a text file for the current note
    try:
        # Ensure filename does not have illegal chars
        cleaned_header = re.sub('[^a-zA-Z0-9\n\.]', ' ', header)
        filename = f'notes/{cleaned_header}.txt'
        with open(filename, 'w') as f:
            # TODO: How to save images in Notes, tables, other data or whether they are out of scope
            f.write(body)
            file_hash = hashlib.sha1(str.encode(body)).hexdigest()
            logger.info(f"Saved note: {filename} with hash: {file_hash}")
            return file_hash
    except Exception as e:
        logger.error(f"Failed to write the note file due to {e}")
        return -1


def main():
    # init mouse and keyboard controllers
    my_mouse = mouse.Controller()
    my_keyboard = keyboard.Controller()

    time.sleep(START_DELAY)

    # Runs save_cur_note until end of notes
    # Detects if the sha1 hash of notes/{header}.txt is already in the dir, if so then quit
    files_written = []
    while True:
        # Open highlighted note
        kh.press_enter(my_keyboard=my_keyboard)
        time.sleep(INPUT_DELAY)

        kh.press_tab(my_keyboard=my_keyboard)
        time.sleep(INPUT_DELAY)

        # Save highlighted note and store its hash
        created_file = save_cur_note(my_mouse, my_keyboard)
        files_written.append(created_file)
        time.sleep(INPUT_DELAY)

        # Return to gallery view
        kh.press_esc(my_keyboard=my_keyboard)
        time.sleep(INPUT_DELAY)

        # Move right to next note
        kh.press_right_arrow(my_keyboard=my_keyboard)
        time.sleep(INPUT_DELAY)
        # If last two notes are same, end of files reached
        if len(files_written) > 2 and files_written[-1] == files_written[-3]:
            logger.info(f"Files written: {files_written} has len {len(files_written)}")
            logger.info("Reached end of notes. Exiting program.")
            break
        elif len(files_written) > 1 and files_written[-1] == files_written[-2]:
            # Return to the start of the current row
            for i in range(len(files_written)):
                kh.press_left_arrow(my_keyboard=my_keyboard)
            # Move down to the next row
            kh.press_down_arrow(my_keyboard=my_keyboard)


if __name__ == '__main__':
    main()
