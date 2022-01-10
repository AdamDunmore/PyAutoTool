import keyboard
import mouse
import time


def morkkeyboard():
    writeY = "Yes"
    writeN = "No"
    write = input("Would you like to write something? Yes or No ")

    if write.lower() == writeY.lower():
        answer = input("Enter Text ")
        autoenter = input("Do you want it to autoenter? Yes or No ")

        while 2 > 1:
            keyboard.write(answer)
            if autoenter == "Yes":
                keyboard.press_and_release("enter")

    if write.lower() == writeN.lower():
        answer = input("Enter Button ")

        while 2 > 1:
            keyboard.press_and_release(answer)

    else:
        print("Invalid Input")

def morkmouse():
    mousestuffL = "Left"
    mousestuffR = "Right"
    mousestuff = input("Would you like to Right or Left click? ")

    if mousestuff.lower() == mousestuffR.lower():
        switchMR()

    if mousestuff.lower() == mousestuffL.lower():
        switchML()

def switchMR():
    global start
    Y = 0
    start = 0
    hotkey = input("Enter hotkey")
    while 2 > 1:

        if keyboard.on_press_key(hotkey) and start == 0:
            print("On")
            start = 1
            time.sleep(0.2)

        if keyboard.on_press_key(hotkey) and start == 1:
            print("Off")
            start = 0
            time.sleep(0.2)

        if start == 1 and Y == 0:
            mouse.click(button="right")
            Y = 1
            time.sleep(1)
            Y = 0
            continue

def switchML():
    global start
    Y = 0
    start = 0
    hotkey = input("Enter hotkey")
    while 2 > 1:

        if keyboard.on_press_key(hotkey) and start == 0:
            print("On")
            start = 1
            time.sleep(0.2)

        if keyboard.on_press_key(hotkey) and start == 1:
            print("Off")
            start = 0
            time.sleep(0.2)

        if start == 1 and Y == 0:
            mouse.click(button="left")
            Y = 1
            time.sleep(1)
            Y = 0
            continue

def question():
    global mork

    morkK = "Keyboard"
    morkM = "Mouse"
    mork = input("What would you like to use? Mouse or Keyboard ")



    if mork.lower() == morkM.lower():
        morkmouse()

    if mork.lower() == morkK.lower():
        morkkeyboard()

question()







