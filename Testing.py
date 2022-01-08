import time
import time
import keyboard
import mouse

start = 0

def switch():
    global start
    hotkey = input("Enter hotkey")
    while 2 > 1:

        if keyboard.is_pressed("hotkey") and start == 0:
           print("On")
           time.sleep(0.2)
           start = 1

        if keyboard.is_pressed("hotkey") and start == 1:

            print("Off")
            time.sleep(0.2)
            start = 0

switch()


