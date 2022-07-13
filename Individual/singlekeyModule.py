#mouse
from tkinter import *
import tkinter as tk
import mouse
import keyboard

SingleKey = tk.Tk()
SingleKey.title("Single Key")

#Key Entry
SingleKeyChoiseLabel = Label(SingleKey, text="Enter Key")
SingleKeyChoiseLabel.grid(row=0,column=0)
SingleKeyChoiseEntry = Entry(SingleKey)
SingleKeyChoiseEntry.grid(row=0,column=1)

#Delay
SingleKeyDelayLabel = Label(SingleKey,text="Enter Delay (in milliseconds)")
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


    def onoff():
        global status
        status = not bool(status)  # Toggle
        print("On" if status else "Off")

    def Event():
        if status == True:
            keyboard.press_and_release(SingleKeyChoiseEntry.get())
            SingleKey.after(int(SingleKeyDelayEntry.get()), Event)
        elif status != True:
            SingleKey.after(int(SingleKeyDelayEntry.get()), Event)

    Event()
    keyboard.add_hotkey(ADKeyEntry.get(), onoff)

#Confirm Choise
ConfirmSK = Button(SingleKey, text="Confirm", command=SingleKeyProcess)
ConfirmSK.grid(row=3, column=0)

def stop():
    keyboard.unhook_all_hotkeys()

StopButton = Button(SingleKey, text="Stop", command=stop)
StopButton.grid(row=3,column=1)

SingleKey.mainloop()