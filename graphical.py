import tkinter as tk
from tkinter import *
import time
import keyboard
import mouse

def Options():
    if InitialOptions.get() == "Single Key":
        SingleKey = tk.Tk()
        SingleKey.title("Single Key")

        #Key Entry
        SingleKeyChoiseLabel = Label(SingleKey, text="Enter Key")
        SingleKeyChoiseLabel.grid(row=0,column=0)
        SingleKeyChoiseEntry = Entry(SingleKey)
        SingleKeyChoiseEntry.grid(row=0,column=1)

        #Delay
        SingleKeyDelayLabel = Label(SingleKey,text="Enter Delay (in Seconds)")
        SingleKeyDelayLabel.grid(row=1,column=0)
        SingleKeyDelayEntry = Entry(SingleKey)
        SingleKeyDelayEntry.grid(row=1,column=1)

        #Activation/Deactivation Key
        ADKeyLabel = Label(SingleKey, text="Enter key for Activation/Deactivation")
        ADKeyLabel.grid(row=2,column=0)
        ADKeyEntry = Entry(SingleKey)
        ADKeyEntry.grid(row=2, column=1)

        #Process
        def SingleKeyProcess():
            global status
            status = False

            def onoff(eventtype):
                global status
                status = not bool(status)  # Toggle
                print("On" if status else "Off")


            ADKey = ADKeyEntry.get()
            keyboard.on_press_key(ADKey, onoff)
            while True:
                if status == True:
                    keyboard.press_and_release(SingleKeyChoiseEntry.get())
                    time.sleep(int(SingleKeyDelayEntry.get()))

        #Confirm Choise
        ConfirmSK = Button(SingleKey, text="Confirm", command=SingleKeyProcess)
        ConfirmSK.grid(row=3, column=0)


    elif InitialOptions.get() == "MultiKey":
        Multikey = tk.Tk()
        Multikey.title("Multikey")

        #Key Entry
        MultikeyChoiseLabel = Label(Multikey, text="Enter Keys")
        MultikeyChoiseLabel.grid(row=0,column=0)
        MultikeyChoiseEntry = Entry(Multikey)
        MultikeyChoiseEntry.grid(row=0,column=1)

        #Delay
        MultikeyDelayLabel = Label(Multikey,text="Enter Delay (in Seconds)")
        MultikeyDelayLabel.grid(row=1,column=0)
        MultikeyDelayEntry = Entry(Multikey)
        MultikeyDelayEntry.grid(row=1,column=1)

        #Activation/Deactivation Key
        ADKeyLabel = Label(Multikey, text="Enter key for Activation/Deactivation")
        ADKeyLabel.grid(row=2,column=0)
        ADKeyEntry = Entry(Multikey)
        ADKeyEntry.grid(row=2, column=1)

        #Process
        def MultiKeyProcess():
            global status
            status = False

            def onoff(eventtype):
                global status
                status = not bool(status)  # Toggle
                print("On" if status else "Off")


            ADKey = ADKeyEntry.get()
            keyboard.on_press_key(ADKey, onoff)
            while True:
                if status == True:
                    keyboard.press_and_release(MultikeyChoiseEntry.get())
                    time.sleep(int(MultikeyDelayEntry.get()))

        #Confirm Choise
        ConfirmMK = Button(Multikey, text="Confirm", command=MultiKeyProcess)
        ConfirmMK.grid(row=3, column=0)

    elif InitialOptions.get() == "Mouse":
        Mouse = tk.Tk()
        Mouse.title("Mouse")

        MouseR = StringVar(master=Mouse)
        MouseR.set("left")

        MouseRadioLabel = Label(Mouse, text="Choose Mouse Button")
        MouseRadioLabel.grid(row=0, column=0)

        MouseRadioLeft = Radiobutton(Mouse, text="Left", variable=MouseR, value="left")
        MouseRadioLeft.grid(column=0,row=1)
        MouseRadioRight = Radiobutton(Mouse,text="Right", variable=MouseR, value="right")
        MouseRadioRight.grid(column=1, row=1)

        #Delay
        MouseDelayLabel = Label(Mouse,text="Enter Delay (in Seconds)")
        MouseDelayLabel.grid(row=2,column=0)
        MouseDelayEntry = Entry(Mouse)
        MouseDelayEntry.grid(row=2,column=1)

        #Activation/Deactivation Key
        ADKeyLabel = Label(Mouse, text="Enter key for Activation/Deactivation")
        ADKeyLabel.grid(row=3,column=0)
        ADKeyEntry = Entry(Mouse)
        ADKeyEntry.grid(row=3, column=1)

        def MouseProcess():
            global status
            status = False

            def onoff(eventtype):
                global status
                status = not bool(status)  # Toggle
                print("On" if status else "Off")

            ADKey = ADKeyEntry.get()
            keyboard.on_press_key(ADKey, onoff)
            while True:
                if status == True:
                    mouse.click(MouseR.get())
                    time.sleep(int(MouseDelayEntry.get()))

        MouseButton = Button(Mouse, text="Confirm", command=MouseProcess)
        MouseButton.grid(row=4, column=0)



window = tk.Tk()
window.title("Options")
window.geometry("220x65")


InitialOptions = StringVar()
InitialOptions.set("Single Key")

OptionsDropDown = OptionMenu(window,InitialOptions,"Single Key", "MultiKey", "Mouse")
OptionsDropDown.pack()
OptionsButton = Button(window, text="Confirm", command=Options)
OptionsButton.pack()

window.mainloop()