import keyboard
import mouse
import time

Mouse = "mouse"
Keyboard = "keyboard"

MouseKeyboard = input("Would you like to use Mouse or Keyboard? ")

if Mouse.lower() == MouseKeyboard.lower():

    Left = "left"
    Right = "right"
    delay = int(input("Choose a delay (in seconds)? "))
    hotkey = input("Choose a hotkey ")
    LeftRight = input("Left or Right? ")

    if LeftRight.lower() == Left.lower():
        status = False
        def onoff(eventtype):
            global status
            status = not status  # Toggle
            print("On" if status else "Off")

        keyboard.on_press_key(hotkey, onoff)

        while True:
            if status == True:
                mouse.click("left")
                time.sleep(delay)

    if LeftRight.lower() == Right.lower():
        status = False
        def onoff(eventtype):
            global status
            status = not status  # Toggle
            print("On" if status else "Off")

        keyboard.on_press_key(hotkey, onoff)

        while True:
            if status == True:
                mouse.click("right")
                time.sleep(delay)









