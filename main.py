import keyboard
import mouse
import time

Mouse = "mouse"
Keyboard = "keyboard"

MouseKeyboard = input("Would you like to use Mouse or Keyboard? ")

if Mouse.lower() == MouseKeyboard.lower():

    Left = "left"
    Right = "right"
    delay = float(input("Choose a delay (in seconds)? "))
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

if MouseKeyboard.lower() == Keyboard.lower():
        Mode_TypeType = "Type"
        Mode_TypeSingleKey = "Key"
        Mode_Hotkey = "Hotkey"

        Type = input("What mode would you like? "Type", "Key" or "Hotkey"?  ")
        delay = float(input("What would you like the delay to be? "))
        hotkey = input("What is your hotkey? ")

        if Mode_TypeType.lower() == Type.lower():
            status = False
            text = input("What would you like to type? ")
            def onoff(eventtype):
                global status
                status = not status  # Toggle
                print("On" if status else "Off")


            keyboard.on_press_key(hotkey, onoff)

            while True:
                if status == True:
                    keyboard.write(text)
                    time.sleep(delay)

        if Mode_TypeSingleKey.lower() == Type.lower():
            status = False
            key = input("What key would you like to enter? ")
            def onoff(eventtype):
                global status
                status = not status  # Toggle
                print("On" if status else "Off")        
            keyboard.on_press_key(hotkey, onoff)        
            while True:
                if status == True:
                    keyboard.press_and_release(key)
                    keyboard.press_and_release("enter")
                    time.sleep(delay)

        if Mode_Hotkey.lower == Type.lower:
            status = False
            hotkey = input #needs finished
            global status
            status = not status  # Toggle
            print("On" if status else "Off")  
        keyboard.on_press_key(hotkey,onoff)
        while True:
            if status == True:
                #needs finished
                time.sleep(delay)







