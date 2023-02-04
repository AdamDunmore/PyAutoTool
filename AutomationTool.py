#Check Lists:
#   --Mouse Hold Feature
#   --Recordable Macros
#   --Themes
#   --Move error messages

from tkinter import *
import keyboard
import mouse
from PIL import ImageTk, Image


EntryColour = "#181A21"
BackgroundColour = "#303443"
ForegroundColour = "#ffffff"
BorderColour = "#414554"

global running
running = False

def stop():
    keyboard.unhook_all_hotkeys()
    global repeat
    repeat = False
    

class Processes:
    def __init__(self, delay, key, buttonKey,AE, Mode,Hold, HoldTime):    
        self.delay = int(delay)
        self.actKey = key
        self.button = buttonKey
        self.status = False
        self.eventStatus = False
        self.AE = AE
        self.Mode = Mode
        self.Hold = Hold
        self.HoldTime = HoldTime
        repeat = True

    def onoff(self):
        self.status = not bool(self.status)  # Toggle
        print("On" if self.status else "Off")

    def Event(self):
        if self.status == True:
            keyboard.press_and_release(self.button)
        if repeat == True:        
            window.after(self.delay, self.Event)

    def MK_Event(self):
        if self.status == True:
            keyboard.write(self.button)
            if self.AE == 1:
                keyboard.send("enter")
        if repeat == True:                
            window.after(self.delay, self.MK_Event)

        

    def Mouse_Event(self):
        print(self.Hold)
        print(self.status)
        if self.status == True and self.Hold == 0:
            mouse.click(self.button)
        elif self.status == True and self.Hold == 1:
            mouse.hold(self.button)
            window.after(self.HoldTime, lambda: mouse.release(self.button))


        if repeat == True:
            window.after(self.delay, self.Mouse_Event)


    def addHotkey(self):
        global repeat
        repeat = True
        keyboard.add_hotkey(self.actKey, self.onoff)
        if self.Mode == "Key":
            self.Event()

        elif self.Mode == "Keys":
            self.MK_Event()

        elif self.Mode == "Mouse":
            self.Mouse_Event()

class FrameConstructor:
    def updateAE(self):    
            self.AEState = self.AE.get()
            print(self.AEState)

    def ToggleMouseHoldTime(self):
        if self.HoldMouse.get() == 1:
            self.HoldMouseLabel.place(x=80,y=60)
            self.HoldMouseLength.place(x=230,y=60)

        elif self.HoldMouse.get() == 0:
            self.HoldMouseLength.place_forget()
            self.HoldMouseLabel.place_forget()


    def __init__(self, keyInput = False, keyInputText = "", AutoEnter = False):
        self.keyInput = bool(keyInput)
        self.keyInputText = keyInputText
        self.AutoEnter = AutoEnter
        self.AE = IntVar()
        self.MouseR = StringVar()
        self.MouseR.set("left")
        self.StopConfirmToggle = True

        self.keys = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
        '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?',
        '`', '~', 'control', 'shift', 'alt', 'tab', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'delete', 'insert'
        ]

        self.mouse_keys = [
        "left", "right", "middle"
        ]

        #Construct Frame
        self.MyFrame = Frame(window, bg=BackgroundColour,width=320, height=132, padx=10, pady=10, highlightthickness=3, highlightbackground=BorderColour, relief="solid")
        self.MyFrame.place(x=140, y=10)

        # Delay
        Label(self.MyFrame, text="Enter Delay (in milliseconds):",fg=ForegroundColour,font=("Segoe UI", 10,"underline"),bg=BackgroundColour).place(x=5,y=32)
        self.DelayEntry = Entry(self.MyFrame,fg=ForegroundColour,font=("Segoe UI", 10),bg=EntryColour,width=16,highlightcolor=BorderColour)
        self.DelayEntry.place(x=178, y=32)


        # Activation/Deactivation Key
        Label(self.MyFrame, text="Enter Toggle Key:", font=("Segoe UI", 10,"underline"),fg=ForegroundColour,bg=BackgroundColour).place(x=130, y=2)
        self.ADKeyEntry = Entry(self.MyFrame, font=("Segoe UI", 10),fg=ForegroundColour, bg=EntryColour,width=7,highlightcolor=BorderColour)
        self.ADKeyEntry.place(x=240,y=2)

        #Key Entry
        if self.keyInput == True:
            self.KeyChoiseLabel = Label(self.MyFrame,font=("Segoe UI",10,"underline"), bg=BackgroundColour,fg=ForegroundColour)
            self.KeyChoiseEntry = Entry(self.MyFrame,font=("Segoe UI",10), bg=EntryColour,fg=ForegroundColour,width=7,highlightcolor=BorderColour)  
            if self.keyInputText == "Key":
                self.KeyChoiseLabel.configure(text="Enter key:")
            
            elif self.keyInputText == "Keys":
                self.KeyChoiseLabel.configure(text="Enter Keys:")
                
            self.KeyChoiseEntry.place(x=75,y=2)
            self.KeyChoiseLabel.place(x=5,y=2)

             


        elif self.keyInput == False:
            #Mouse Buttons
            Radiobutton(self.MyFrame, variable=self.MouseR,text="Left", value="left",bg=BackgroundColour, activeforeground=EntryColour, activebackground=BackgroundColour,selectcolor=EntryColour, fg=ForegroundColour).place(x=5, y=2)
            Radiobutton(self.MyFrame, variable=self.MouseR,text="Right", value="right",bg=BackgroundColour, activeforeground=EntryColour, activebackground=BackgroundColour,selectcolor=EntryColour, fg=ForegroundColour).place(x=55, y=2,)

            self.HoldMouseLabel = Label(self.MyFrame, text="Hold Time milliseconds:", bg=BackgroundColour, fg=ForegroundColour,font=("Segoe UI", 10,"underline"))
            self.HoldMouseLength = Entry(self.MyFrame, bg=EntryColour, fg=ForegroundColour,width=10)

            self.HoldMouse = IntVar()
            self.HoldMouseButton=Checkbutton(self.MyFrame,  text="Hold",foreground=ForegroundColour,background=BackgroundColour,  variable=self.HoldMouse, selectcolor=EntryColour,activebackground=BackgroundColour,activeforeground=ForegroundColour,command=self.ToggleMouseHoldTime)
            self.HoldMouseButton.place(x=240, y=90)




        #Error Label
        self.ErrorLabel = Label(self.MyFrame, text="", bg=BackgroundColour, fg=ForegroundColour, font=("Segoe UI", 7),width=20, height=1)
        self.ErrorLabel.place(x=90,y=70)


        #Confirm Choise
        self.Confirm = Button(self.MyFrame, text="Confirm", command=self.start,height=1, bg=BackgroundColour, fg=ForegroundColour, activebackground=EntryColour, activeforeground=ForegroundColour)
        if running == False:
            self.Confirm.place(x=5, y=80)
        
        #Stop
        self.Stop = Button(self.MyFrame, text="Stop", command=lambda: [stop(), self.stopRunning() ],height=1, bg=BackgroundColour, fg=ForegroundColour, activebackground=EntryColour, activeforeground=ForegroundColour)
        if running == True:
            self.Stop.place(x=5, y=80)
       
        #Status Icon
        self.iconImageStopped = Image.open("img/statusStop.png")
        self.iconImageGo = Image.open("img/statusGo.png")
        self.iconImageGo = self.iconImageGo.resize((25,25), Image.LANCZOS)
        self.iconImageStopped = self.iconImageStopped.resize((25,25), Image.LANCZOS)
        
        if running == True:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageGo)
        
        elif running == False:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageStopped)
        
        self.imageStatusLabel = Label(self.MyFrame,image=self.iconImageTk, bg=BackgroundColour)
        self.imageStatusLabel.place(x=65,y=80)
    

        if self.AutoEnter == True:
            # AutoEnter
            Checkbutton(self.MyFrame, text="AE",foreground=ForegroundColour,background=BackgroundColour,  variable=self.AE, selectcolor=EntryColour,activebackground=BackgroundColour,activeforeground=ForegroundColour,command=self.updateAE).place(x=250,y=80)



    def updateRunning(self):
        global running
        if running == True:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageGo)
        
        elif running == False:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageStopped)

        self.imageStatusLabel.configure(image=self.iconImageTk)


    def start(self):
        #Error Detection
        keysString = ""
        if str(self.DelayEntry.get()).isdigit() != True:
            #Tell user to use an int
            self.ErrorLabel.configure(text="You must use a whole number")
 
        elif str(self.ADKeyEntry.get()) not in self.keys:
            self.ErrorLabel.configure(text="Please use key from list for activation key")

            for counter in self.keys:
                keysString += counter + ","

            keyWindow = Tk()
            keyWindow.title("List")
            keyWindow.attributes("-topmost",True)
            Label(keyWindow, text=keysString, wraplength=200).pack()

        elif self.keyInputText == "Key" and str(self.KeyChoiseEntry.get()) not in self.keys:
            self.ErrorLabel.configure(text="Please use key from list for autokey")

            for counter in self.keys:
                keysString += counter + ","

            keyWindow = Tk()
            keyWindow.title("List")
            keyWindow.attributes("-topmost",True)
            Label(keyWindow, text=keysString, wraplength=200).pack()

        else:
            if self.keyInput == True:
                self.button = self.KeyChoiseEntry.get()

            elif self.keyInput == False:
                self.button = self.MouseR.get()

                if self.HoldMouse.get() == 0:
                    self.MouseHoldTime = 0

                else:
                    self.MouseHoldTime = int(self.HoldMouseLength.get())


            self.Process = Processes(self.DelayEntry.get(), self.ADKeyEntry.get(), self.button, self.AE.get(),self.keyInputText, self.HoldMouse.get(), self.MouseHoldTime)
            self.Process.addHotkey()
            global running
            running = True
            self.updateRunning()

            #Removes error message
            self.ErrorLabel.configure(text="")

            #Toggles Confirm/Stop Button
            self.Stop.place(x=5, y=80)
            self.Confirm.place_forget()


    def stopRunning(self):
        global running
        running = False
        self.updateRunning()
        self.Confirm.place(x=5, y=80)
        self.Stop.place_forget()

def singlekeyFun():  
    singleKeyFrame = FrameConstructor(keyInput = True,keyInputText= "Key",AutoEnter= False)
    
def multikeyFun():
    multikeyFrame = FrameConstructor(keyInput = True,keyInputText= "Keys",AutoEnter= True)

def mouseFun():
    mouseFrame = FrameConstructor(keyInput = False,keyInputText = "Mouse",AutoEnter = False)

window = Tk()
window.title("Autoclicker")
window.geometry("470x150")
window.configure(bg="#525665")
window.resizable(False,False)
window.attributes("-topmost",True)

optionsFrame = Frame(window, bg=BackgroundColour,width=120, height=132, highlightthickness=3, highlightbackground=BorderColour, relief="solid")
optionsFrame.place(x=10, y=10)

InitialOptions = StringVar()
InitialOptions.set("Single Key")

singlekeyFun()

Radiobutton(optionsFrame, variable=InitialOptions,text="Single Key", value="Single Key", font=("Segoe UI", 10), bg=BackgroundColour,activebackground=BackgroundColour,fg=ForegroundColour, activeforeground=EntryColour,selectcolor=EntryColour, command=singlekeyFun).place(x=5, y=10)
Radiobutton(optionsFrame, variable=InitialOptions,text="MultiKey", value="Multi Key",font=("Segoe UI", 10), bg=BackgroundColour,activebackground=BackgroundColour, activeforeground=EntryColour,fg=ForegroundColour,selectcolor=EntryColour, command=multikeyFun).place(x=5, y=50)
Radiobutton(optionsFrame, variable=InitialOptions,text="Mouse", value="Mouse", font=("Segoe UI", 10), bg=BackgroundColour,activebackground=BackgroundColour, activeforeground=EntryColour,fg=ForegroundColour,selectcolor=EntryColour,command=mouseFun).place(x=5, y=90)

window.mainloop()