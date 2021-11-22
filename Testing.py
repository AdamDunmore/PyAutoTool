import keyboard
import time
import mouse


def check_switch():

    while 2 > 1:
        keyboard.wait("esc")
        switch = 1
        print(switch)

        keyboard.wait("p")
        switch = 0
        print(switch)



print(check_switch())

while 2 > 1:
    if check_switch() == 1:
        print("Ya")
        time.sleep(1)
