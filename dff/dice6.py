import keyboard
import time
import sys

def Meepo_key():
    keyboard.send('w')
    time.sleep(2)
    keyboard.send('space')

while True:
    if keyboard.read_key() == ",":
        break
    keyboard.add_hotkey('m', Meepo_key)
