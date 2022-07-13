from tkinter import *
import tkinter as tk
import keyboard
import mouse

Mouse = tk.Tk()
Mouse.title("Mouse")

#RadioButton
MouseR = StringVar(master=Mouse)
MouseR.set("left")

MouseRadioLabel = Label(Mouse, text="Choose Mouse Button")
MouseRadioLabel.grid(row=0, column=0)
MouseRadioLeft = Radiobutton(Mouse, text="Left", variable=MouseR, value="left")
MouseRadioLeft.grid(column=0, row=1)
MouseRadioRight = Radiobutton(Mouse, text="Right", variable=MouseR, value="right")
MouseRadioRight.grid(column=1, row=1)

# Delay
MouseDelayLabel = Label(Mouse, text="Enter Delay (in milliseconds)")
MouseDelayLabel.grid(row=2, column=0)
MouseDelayEntry = Entry(Mouse)
MouseDelayEntry.grid(row=2, column=1)

# Activation/Deactivation Key
ADKeyLabel = Label(Mouse, text="Enter key for Activation/Deactivation")
ADKeyLabel.grid(row=3, column=0)
ADKeyEntry = Entry(Mouse)
ADKeyEntry.grid(row=3, column=1)


#messy
def MouseProcess():
    global status
    status = False

    def onoff():
            global status
            status = not bool(status)  # Toggle
            print("On" if status else "Off")


    def Event():

        if status == True:
            mouse.click(MouseR.get())
            Mouse.after(int(MouseDelayEntry.get()), Event)

        elif status != True:
            Mouse.after(int(MouseDelayEntry.get()), Event)
    Event()

    keyboard.add_hotkey(ADKeyEntry.get(),onoff)


MouseButton = Button(Mouse, text="Confirm", command=MouseProcess)
MouseButton.grid(row=4, column=0)
def unhook():
    keyboard.unhook_all_hotkeys()

StopButton =Button(Mouse, text="Stop", command=unhook)
StopButton.grid(row=4,column=1)

Mouse.mainloop()