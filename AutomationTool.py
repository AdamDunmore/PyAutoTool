from tkinter import *
import keyboard
import mouse

def stop():
    keyboard.unhook_all_hotkeys()

class Processes:

    def __init__(self, delay, key, buttonKey,Frame):     
        print(self)   
        self.delay = int(delay)
        self.actKey = key
        self.button = buttonKey
        self.status = False
        self.Frame = Frame
        self.eventStatus = False

    def onoff(self):
        if self.eventStatus == False:
            self.Event()
            self.eventStatus = True

        self.status = not bool(self.status)  # Toggle
        print("On" if self.status else "Off")

    def Event(self):
        print(self, "Event")
        if self.status == True:
            #keyboard.press_and_release(self.button)
            print("Hey")
            self.Frame.after(self.delay, Event)
        elif self.status == False:
            self.Frame.after(self.delay, Event)

    def addHotkey(self):
        print(self, "Add Hotkey")
        keyboard.add_hotkey(self.actKey, self.onoff)
        self.Event()



class FrameConstructor:
    def __init__(self):


        #Construct Window
        self.MyFrame = Frame(window, bg="#404040",width=320, height=130, padx=10, pady=10, highlightthickness=3, highlightbackground="grey", relief="solid")
        self.MyFrame.place(x=140, y=10)

        # Delay
        self.DelayLabel = Label(self.MyFrame, text="Enter Delay (in milliconds):",fg="white",font=("Segoe UI", 10,"underline"),bg="#404040")
        self.DelayEntry = Entry(self.MyFrame,fg="white",font=("Segoe UI", 10),bg="grey",width=18)
        self.DelayLabel.place(x=5,y=32)
        self.DelayEntry.place(x=165, y=32)

        # Activation/Deactivation Key
        self.ADKeyLabel = Label(self.MyFrame, text="Enter Toggle Key:", font=("Segoe UI", 10,"underline"),fg="white",bg="#404040")
        self.ADKeyEntry = Entry(self.MyFrame, font=("Segoe UI", 10),fg="white", bg="grey",width=7)
        self.ADKeyLabel.place(x=130, y=2)
        self.ADKeyEntry.place(x=240,y=2)

        #Confirm Choise
        self.ConfirmSK = Button(self.MyFrame, text="Confirm", command=self.start,height=1, bg="#404040", fg="white", activebackground="grey", activeforeground="white")
        self.ConfirmSK.place(x=5, y=80)
        #Stop
        self.StopButton = Button(self.MyFrame, text="Stop", command=stop,height=1, bg="#404040", fg="white", activebackground="grey", activeforeground="white")
        self.StopButton.place(x=65, y=80)

    def start(self):
        self.Process = Processes(self.DelayEntry.get(), self.ADKeyEntry.get(),'a',self.MyFrame)
        self.Process.addHotkey()


        




def singlekeyFun():
    
    singleKeyFrame = FrameConstructor()
    
"""
    # Key Entry
    SingleKeyChoiseLabel = Label(singleKeyFrame.MyFrame, text="Enter Key:",font=("Segoe UI",10,"underline"), bg="#404040",fg="white")
    SingleKeyChoiseEntry = Entry(singleKeyFrame.MyFrame,font=("Segoe UI",10), bg="grey",fg="white",width=7)
    SingleKeyChoiseLabel.place(x=5,y=2)
    SingleKeyChoiseEntry.place(x=70,y=2)    
 


    def start():
        singleKey = Processes(SingleKeyDelayEntry.get(),ADKeyEntry.get(),SingleKeyChoiseEntry.get(), SingleKey)
        singleKey.addHotkey()


    """

                         #--------------------------------------------------------------------------------------------#
"""def multikeyFun():
    Multikey = Frame(window, bg="#404040", width=320, height=130, padx=10, pady=10, highlightthickness=3, highlightbackground="grey", relief="solid")
    Multikey.place(x=140, y=10)

    # Key Entry
    MultikeyChoiseLabel = Label(Multikey, text="Enter Sentance:",bg="#404040",fg="white", font=("Segoe UI", 10, "underline"))
    MultikeyChoiseEntry = Entry(Multikey,fg="white", bg="grey", font=("Segoe UI", 10), width=26)
    MultikeyChoiseLabel.place(x=5, y=2)
    MultikeyChoiseEntry.place(x=100,y=2)

    # Delay
    MultikeyDelayLabel = Label(Multikey, text="Enter Delay (in milliseconds):", bg="#404040", fg="white", font=("Segoe UI", 10, "underline"))
    MultikeyDelayEntry = Entry(Multikey, bg="grey", fg="white", font=("Segoe UI", 10), width=15)
    MultikeyDelayLabel.place(x=5, y=30)
    MultikeyDelayEntry.place(x=180, y=30)

    # Activation/Deactivation Key
    ADKeyLabel = Label(Multikey, text="Enter key for Activation/Deactivation:", bg="#404040", fg="white", font=("Segoe UI", 10,"underline"))
    ADKeyEntry = Entry(Multikey, bg="grey", fg="white", font=("Segoe UI", 10), width=6)
    ADKeyLabel.place(x=5, y=55)
    ADKeyEntry.place(x=230, y=55)

    # AutoEnter
    AE = IntVar()
    AEButton = Checkbutton(Multikey)
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
    ConfirmMK = Button(Multikey, text="Confirm", command=MultikeyProcess, height=1, bg="#404040", fg="white", activebackground="grey", activeforeground="white")
    ConfirmMK.place(x=5, y=80)

    def stop():
        keyboard.unhook_all_hotkeys()

    stopButton = Button(Multikey, text="Stop", command=stop,height=1, bg="#404040", fg="white", activebackground="grey", activeforeground="white")
    stopButton.place(x=65, y=80)

def mouseFun():
    Mouse = Frame(window,bg="#404040", width=320, height=130, padx=10, pady=10, highlightthickness=3, highlightbackground="grey", relief="solid")
    Mouse.place(x=140 , y=10)

    MouseR = StringVar(master=Mouse)
    MouseR.set("left")

    MouseRadioLabel = Label(Mouse, text="Choose Mouse Button:", font=("Segoe UI", 10, "underline"),fg="white", bg="#404040")
    MouseRadioLeft = Radiobutton(Mouse, variable=MouseR, value="left",bg="#404040", activeforeground="grey", activebackground="#404040")
    MouseRadioRight = Radiobutton(Mouse, variable=MouseR, value="right",bg="#404040", activeforeground="grey", activebackground="#404040")
    MouseRadioLeftLabel = Label(Mouse,text="Left", fg="white", font=("Segoe UI", 10),bg="#404040")    
    MouseRadioRightLabel = Label(Mouse,text="Right", fg="white", font=("Segoe UI", 10),bg="#404040")
    MouseRadioLeftLabel.place(x=170,y=2)
    MouseRadioRightLabel.place(x=220,y=2)
    MouseRadioLabel.place(x=5, y=2)
    MouseRadioLeft.place(x=150, y=2)
    MouseRadioRight.place(x=200, y=2,)

    # Delay
    MouseDelayLabel = Label(Mouse, text="Enter Delay (in milliseconds):", font=("Segoe UI", 10, "underline"), fg="white", bg="#404040")
    MouseDelayEntry = Entry(Mouse ,bg="grey", fg="white", font=("Segoe UI", 10), width=8)
    MouseDelayLabel.place(x=5, y=30)
    MouseDelayEntry.place(x=180, y=30)

    # Activation/Deactivation Key
    ADKeyLabel = Label(Mouse, text="Enter key for Activation/Deactivation:", font=("Segoe UI", 10, "underline"), fg="white", bg="#404040")
    ADKeyEntry = Entry(Mouse, bg="grey", fg="white", font=("Segoe UI", 10), width=8)
    ADKeyLabel.place(x=5, y=60)
    ADKeyEntry.place(x=225, y=60)
    # messy
    def MouseProcess():
        global status
        status = False
        def onoff():
                global status
                status = not bool(status)  # Toggle
                print("On" if status else "Off")

        def Event():
            if status:
                mouse.click(MouseR.get())
                Mouse.after(int(MouseDelayEntry.get()), Event)

            elif status != True:
                Mouse.after(int(MouseDelayEntry.get()), Event)


        Event()

        keyboard.add_hotkey(ADKeyEntry.get(), onoff)

    MouseButton = Button(Mouse, text="Confirm", command=MouseProcess, height=1, bg="#404040", fg="white", activebackground="grey", activeforeground="white")
    MouseButton.place(x=5, y=85)

    def unhook():
        keyboard.unhook_all_hotkeys()
        global status
        status = False

    StopButton = Button(Mouse, text="Stop", command=unhook, height=1, bg="#404040", fg="white", activebackground="grey", activeforeground="white")
    StopButton.place(x=65 , y=85)

"""

window = Tk()
window.title("Options")
window.geometry("470x150")
window.configure(bg="black")
window.attributes("-topmost",True)

optionsFrame = Frame(window, bg="#404040",width=120, height=132, highlightthickness=3, highlightbackground="grey", relief="solid")
optionsFrame.place(x=10, y=10)

InitialOptions = StringVar()
InitialOptions.set("Single Key")

singlekeyFun()

OptionsRaidioButton1 = Radiobutton(optionsFrame, variable=InitialOptions, value="Single Key", font=("Segoe UI", 10), bg="#404040",activebackground="#404040", activeforeground="grey", command=singlekeyFun)
"""OptionsRaidioButton2 = Radiobutton(optionsFrame, variable=InitialOptions, value="Multi Key",font=("Segoe UI", 10), bg="#404040",activebackground="#404040", activeforeground="grey", command=multikeyFun)
OptionsRaidioButton3 = Radiobutton(optionsFrame, variable=InitialOptions, value="Mouse", font=("Segoe UI", 10), bg="#404040",activebackground="#404040", activeforeground="grey",command=mouseFun)"""
OptionsRaidioButton1Label = Label(optionsFrame, text="Single Key", fg="white", font=("Segoe UI", 10),bg="#404040") 
OptionsRaidioButton2Label = Label(optionsFrame, text="Multi Key", fg="white", font=("Segoe UI", 10),bg="#404040")
OptionsRaidioButton3Label = Label(optionsFrame, text="Mouse", fg="white", font=("Segoe UI", 10),bg="#404040")
OptionsRaidioButton1.place(x=5, y=10)
"""
OptionsRaidioButton2.place(x=5, y=50)
OptionsRaidioButton3.place(x=5, y=90)"""
OptionsRaidioButton1Label.place(x=25,y=10)
OptionsRaidioButton2Label.place(x=25,y=50)
OptionsRaidioButton3Label.place(x=25,y=90)

window.mainloop()
