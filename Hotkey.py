import keyboard
import mouse
import time

def question():
    global mork

    morkK = "Keyboard"
    morkM = "Mouse"
    mork = input("What would you like to use? Mouse or Keyboard ")

    if mork.lower() == morkM.lower():
        def mouse():
            mousestuff = input("Would you like to Right or Left click? ")
            delay = input("What would you like the delay to be (Number is Seconds)")

            delay = int(delay)

            if mousestuff == "Right":
                print("placeholder")
            if mousestuff == "Left":
                print("placeholder")

    if mork.lower() == morkK.lower():
        def keyboard():
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


