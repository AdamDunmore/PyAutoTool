import tkinter as tk
from tkinter import *
import keyboard
import mouse

def Options():
    if InitialOptions.get() == "Single Key":
        SingleKey = tk.Tk()
        SingleKey.title("Single Key")

        # Key Entry
        SingleKeyChoiseLabel = Label(SingleKey, text="Enter Key")
        SingleKeyChoiseLabel.grid(row=0, column=0)
        SingleKeyChoiseEntry = Entry(SingleKey)
        SingleKeyChoiseEntry.grid(row=0, column=1)

        # Delay
        SingleKeyDelayLabel = Label(SingleKey, text="Enter Delay (in milliseconds)")
        SingleKeyDelayLabel.grid(row=1, column=0)
        SingleKeyDelayEntry = Entry(SingleKey)
        SingleKeyDelayEntry.grid(row=1, column=1)

        # Activation/Deactivation Key
        ADKeyLabel = Label(SingleKey, text="Enter key for Activation/Deactivation")
        ADKeyLabel.grid(row=2, column=0)
        ADKeyEntry = Entry(SingleKey)
        ADKeyEntry.grid(row=2, column=1)

        # Process
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

        # Confirm Choise
        ConfirmSK = Button(SingleKey, text="Confirm", command=SingleKeyProcess)
        ConfirmSK.grid(row=3, column=0)

        def stop():
            keyboard.unhook_all_hotkeys()

        StopButton = Button(SingleKey, text="Stop", command=stop)
        StopButton.grid(row=3, column=1)


    elif InitialOptions.get() == "MultiKey":
        Multikey = tk.Tk()
        Multikey.title("Multikey")

        # Key Entry
        MultikeyChoiseLabel = Label(Multikey, text="Enter Sentance")
        MultikeyChoiseLabel.grid(row=0, column=0)
        MultikeyChoiseEntry = Entry(Multikey)
        MultikeyChoiseEntry.grid(row=0, column=1)

        # Delay
        MultikeyDelayLabel = Label(Multikey, text="Enter Delay (in milliseconds)")
        MultikeyDelayLabel.grid(row=1, column=0)
        MultikeyDelayEntry = Entry(Multikey)
        MultikeyDelayEntry.grid(row=1, column=1)

        # Activation/Deactivation Key
        ADKeyLabel = Label(Multikey, text="Enter key for Activation/Deactivation")
        ADKeyLabel.grid(row=2, column=0)
        ADKeyEntry = Entry(Multikey)
        ADKeyEntry.grid(row=2, column=1)

        # AutoEnter
        AE = StringVar(master=Multikey)
        AE.set("No AutoEnter")

        AE1 = Radiobutton(Multikey, text="No AutoEnter", variable=AE, value="No AutoEnter")
        AE1.grid(row=3, column=0)

        AE2 = Radiobutton(Multikey, text="AutoEnter", variable=AE, value="AutoEnter")
        AE2.grid(row=3, column=1)

        # Process
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

        # Confirm Choise
        ConfirmMK = Button(Multikey, text="Confirm", command=MultikeyProcess)
        ConfirmMK.grid(row=4, column=0)

        def stop():
            keyboard.unhook_all_hotkeys()

        stopButton = Button(Multikey, text="Stop", command=stop)
        stopButton.grid(row=4, column=1)

    elif InitialOptions.get() == "Mouse":
        Mouse = tk.Tk()
        Mouse.title("Mouse")

        # RadioButton
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

        # messy
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

            keyboard.add_hotkey(ADKeyEntry.get(), onoff)

        MouseButton = Button(Mouse, text="Confirm", command=MouseProcess)
        MouseButton.grid(row=4, column=0)

        def unhook():
            keyboard.unhook_all_hotkeys()

        StopButton = Button(Mouse, text="Stop", command=unhook)
        StopButton.grid(row=4, column=1)


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