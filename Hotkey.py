import keyboard
import mouse
import time

mork = input("What would you like to use? Mouse or Keyboard ")


if mork == "Mouse":

    hotkey = input("Enter Hotkey ")
    end_hotkey = input("Enter ending hotkey ")
    mousestuff = input("Would you like to Right or Left click? ")
    delay = input("What would you like the delay to be (Number is Seconds)")

    delay = int(delay)

    if mousestuff == "Right":

        keyboard.wait(hotkey)
        time.sleep(1)

        while 2 > 1:
                time.sleep(delay)
                mouse.right_click()
                print("Complete")

                if keyboard.read_key(end_hotkey):
                    break

                else:
                    print("Fail")

    if mousestuff == "Left":

        keyboard.wait(hotkey)
        time.sleep(1)

        while 2 > 1:
                time.sleep(delay)
                mouse.click()
                print("Complete")

                if keyboard.read_key(end_hotkey):
                    print("break")
                    break


    else:
        print("Invalid Input")

if mork == "Keyboard":

    true = input("Would you like to write something? Yes or No ")

    if true == "Yes":
        hotkey = input("Enter Hotkey ")
        answer = input("Enter Text ")
        autoenter = input("Do you want it to autoenter? Yes or No ")

        while 2 > 1:
            keyboard.wait(hotkey)
            keyboard.write(answer)
            if autoenter == "Yes":
                keyboard.press_and_release("enter")
                print("Complete")
    if true == "No":
        hotkey = input("Enter Hotkey ")
        answer = input("Enter Button ")

        while 2 > 1:
            keyboard.wait(hotkey)
            keyboard.press_and_release(answer)
            print("Complete")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
