import keyboard
import time
import threading

stop_spammming = False

def spam_enter():
    while not stop_spammming:
        keyboard.press_and_release('enter')
        time.sleep(0.1)
def start_spam():
    global stop_spammming
    stop_spammming = False
    threading.Thread(target=spam_enter).start()
def stop_spam():
    global stop_spammming
    stop_spammming = True

print("Pressione F8 para iniciar e F9 para desligar")

keyboard.add_hotkey('F8', start_spam)
keyboard.add_hotkey('F9', stop_spam)

keyboard.wait('esc')