import tkinter as tk
from tkinter import *
import keyboard


Multikey = tk.Tk()
Multikey.title("Multikey")

#Key Entry
MultikeyChoiseLabel = Label(Multikey, text="Enter Sentance")
MultikeyChoiseLabel.grid(row=0,column=0)
MultikeyChoiseEntry = Entry(Multikey)
MultikeyChoiseEntry.grid(row=0,column=1)

#Delay
MultikeyDelayLabel = Label(Multikey,text="Enter Delay (in milliseconds)")
MultikeyDelayLabel.grid(row=1,column=0)
MultikeyDelayEntry = Entry(Multikey)
MultikeyDelayEntry.grid(row=1,column=1)

#Activation/Deactivation Key
ADKeyLabel = Label(Multikey, text="Enter key for Activation/Deactivation")
ADKeyLabel.grid(row=2,column=0)
ADKeyEntry = Entry(Multikey)
ADKeyEntry.grid(row=2, column=1)

#AutoEnter
AE = StringVar(master=Multikey)
AE.set("No AutoEnter")

AE1 = Radiobutton(Multikey, text="No AutoEnter", variable=AE, value="No AutoEnter")
AE1.grid(row=3,column=0)

AE2 = Radiobutton(Multikey,text="AutoEnter", variable=AE, value="AutoEnter")
AE2.grid(row=3,column=1)

#Process
def MultikeyProcess():
    global status
    status = False


    def onoff():
        global status
        status = not bool(status)  # Toggle
        print("On" if status else "Off")

    def Event():
        if status == True:
            keyboard.write(MultikeyChoiseEntry.get())
            if AE.get() == "AutoEnter":
                keyboard.send("enter")

            Multikey.after(int(MultikeyDelayEntry.get()), Event)
        elif status != True:
            Multikey.after(int(MultikeyDelayEntry.get()), Event)

    Event()
    keyboard.add_hotkey(ADKeyEntry.get(), onoff)

#Confirm Choise
ConfirmMK = Button(Multikey, text="Confirm", command=MultikeyProcess)
ConfirmMK.grid(row=4, column=0)

def stop():
    keyboard.unhook_all_hotkeys()
stopButton = Button(Multikey, text="Stop", command=stop)
stopButton.grid(row=4,column=1)

Multikey.mainloop()
