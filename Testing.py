import keyboard
import time
import mouse

def check_switch():
    switch = 0
    while 2 > 1:

        if keyboard.read_key("esc"):
            switch = 1
            print(switch)
            continue

check_switch()