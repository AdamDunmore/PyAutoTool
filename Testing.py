import time
import keyboard
import mouse

start = 0

def check_start():
    global start
    while 2 > 1:

        if keyboard.is_pressed("F5") and start == 0:
           print("On")
           time.sleep(0.2)
           start = 1

        if keyboard.is_pressed("F5") and start == 1:

            print("Off")
            time.sleep(0.2)
            start = 0

check_start()

