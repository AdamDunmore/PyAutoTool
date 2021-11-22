import keyboard
import mouse
import time

mork = input("What would you like to use? Mouse or Keyboard ")


if mork == "Mouse":

    hotkey = input("Enter Hotkey ")
    end_hotkey = input("Enter ending hotkey ")
    mousestuff = input("Would you like to Right or Left click? ")
    delay = input("What would you like the delay to be (Number is Seconds) ")

    delay = int(delay)

    if mousestuff == "Right":

        keyboard.wait(hotkey)
        time.sleep(1)

        while 2 > 1:
                time.sleep(1)
                mouse.right_click()
                print("Complete")

                if keyboard.read_key(end_hotkey):
                    break

                else:
                    print("Fail")

    if mousestuff == "Left":

        keyboard.wait(hotkey)
        ("Issue")
        time.sleep(1)

        while 2 > 1:
            mouse.click()
            print("Complete")

            if keyboard.read_key(end_hotkey):
                print("break")
                break


    else:
        print("Invalid Input")




