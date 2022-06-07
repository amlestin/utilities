import logging
from pynput import mouse, keyboard

logging.basicConfig()
logger = logging.getLogger("notes-exporter")
logger.setLevel(logging.INFO)


def press_and_release(my_keyboard, key):
    my_keyboard.press(key)
    my_keyboard.release(key) 

# Press and release ESC
def press_esc(my_keyboard):
    press_and_release(my_keyboard, keyboard.Key.esc)
    logger.info("Press and release ESC")

# Press and release right arrow key
def press_right_arrow(my_keyboard):
    press_and_release(my_keyboard, keyboard.Key.right)
    logger.info("Press and release right arrow key")


# Press and release left arrow key
def press_left_arrow(my_keyboard):
    press_and_release(my_keyboard, keyboard.Key.left)
    logger.info("Press and release left arrow key")


# Press and release down arrow key
def press_down_arrow(my_keyboard):
    press_and_release(my_keyboard, keyboard.Key.down)
    logger.info("Press and release down arrow key")


# Press cmd+2 to activate gallery view
def press_cmd_2(my_keyboard):
    my_keyboard.press(keyboard.Key.cmd)
    my_keyboard.press('2')
    my_keyboard.release(keyboard.Key.cmd)
    my_keyboard.release('2')
    logger.info("Press cmd+2 to activate gallery view")


# Press and release cmd+a
def select_all_text(my_keyboard):
    my_keyboard.press(keyboard.Key.cmd)
    my_keyboard.press('a')
    my_keyboard.release(keyboard.Key.cmd)
    my_keyboard.release('a')
    logger.info("Press and release cmd+a")


# Press and release cmd+c
def copy_text(my_keyboard):
    my_keyboard.press(keyboard.Key.cmd)
    my_keyboard.press('c')
    my_keyboard.release(keyboard.Key.cmd)
    my_keyboard.release('c')
    logger.info("Press and release cmd+c")


# Press and release enter key
def press_enter(my_keyboard):
    press_and_release(my_keyboard, keyboard.Key.enter)
    logger.info("Press and release enter key")


# Press and release tab key to select opened note's text
def press_tab(my_keyboard):
    press_and_release(my_keyboard, keyboard.Key.tab)
    logger.info("Press and release tab key")

