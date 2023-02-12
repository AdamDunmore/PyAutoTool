#Check Lists:
#   --Recordable Macros
#   --Themes
#   --Add memory

from tkinter import *
import keyboard
import mouse
from PIL import ImageTk, Image
from json import load, dumps
import os
from os import getlogin, mkdir




class App(Tk):

    def setup(self):
        #Checks title bar
        self.titleBar = Frame(self,width=470,bg=self.BackgroundColour)
        if self.settingsDict["titleBarStatus"] == True:
            def move_window(event):
                self.geometry(f"+{event.x_root}+{event.y_root}")
            #Creates title bar
            self.overrideredirect(True)
            self.titleBar.bind("<B1-Motion>",move_window)
            titleLabel = Label(self.titleBar, text="AutoClicker",bg=self.BackgroundColour,fg=self.ForegroundColour,height=1).pack(anchor="center", pady=5)
            titleBarClose = Button(self.titleBar,text="X",command=lambda:self.destroy(),bg=self.BackgroundColour,fg=self.ForegroundColour,activebackground=self.BackgroundColour,border=0,height=1).place(x=445,y=5)
            self.titleBar.pack(expand=1, fill=X,anchor=N)
            self.AutoToolLabel.place_forget()
            self.ToggleCustomTitleBarButton.configure(text="On")

        else:
            self.ToggleCustomTitleBarButton.configure(text="Off")
            self.titleBar.destroy()
            self.overrideredirect(False)
            self.AutoToolLabel.place(x=8,y=5)

    def singlekeyFun(self):
            singleKeyFrame = FrameConstructor(keyInput = True,keyInputText= "Key",AutoEnter= False)
        
    def multikeyFun(self):
        multikeyFrame = FrameConstructor(keyInput = True,keyInputText= "Keys",AutoEnter= True)

    def mouseFun(self):
        mouseFrame = FrameConstructor(keyInput = False,keyInputText = "Mouse",AutoEnter = False)

    def ToggleCustomTitleBar(self):
        if self.settingsDict["titleBarStatus"] == False:
            self.titleBar = Frame(self,width=470,bg=self.BackgroundColour)
            def move_window(event):
                self.geometry(f"+{event.x_root}+{event.y_root}")
            #Creates title bar
            self.overrideredirect(True)
            self.titleBar.bind("<B1-Motion>",move_window)
            titleLabel = Label(self.titleBar, text="AutoClicker",bg=self.BackgroundColour,fg=self.ForegroundColour,height=1)
            titleLabel.pack(anchor="center", pady=5)
            titleBarClose = Button(self.titleBar,text="X",command=lambda:self.destroy(),bg=self.BackgroundColour,fg=self.ForegroundColour,activebackground=self.BackgroundColour,border=0,height=1)
            titleBarClose.place(x=445,y=5)
            self.titleBar.pack(expand=1, fill=X,anchor=N)
            self.AutoToolLabel.place_forget()
            self.ToggleCustomTitleBarButton.configure(text="On")

            self.settingsDict["titleBarStatus"] = True

        else:
            self.ToggleCustomTitleBarButton.configure(text="Off")
            self.overrideredirect(False)
            self.AutoToolLabel.place(x=8,y=5)
            self.titleBar.pack_forget()
            self.settingsDict["titleBarStatus"] = False

    def stop(self):
        keyboard.unhook_all_hotkeys()
        self.repeat = False

    def openSettings(self):
        if self.SettingsStatus == False:
            self.Settings.place(x=10,y=45)
            self.Settings.tkraise() 
            self.SettingsStatus = True
        else:
            self.Settings.place_forget()
            self.SettingsStatus = False

    def __init__(self):
        super().__init__() 
        
        self.title("Autoclicker")
        self.geometry("470x230+0+0")
        self.configure(bg="#525665")
        self.resizable(False,False)
        self.attributes("-topmost",True)

        #Colours
        self.EntryColour = "#181A21"
        self.BackgroundColour = "#303443"
        self.ForegroundColour = "#ffffff"
        self.BorderColour = "#414554"
        self.uiFont = "Segoe UI"

        #Gets path and sets up directory
        self.username = getlogin()
        self.LocalLowPath = f"C:/Users/{self.username}/AppData/LocalLow/PyAutoTool"

        firstTime = 0
        if not os.path.exists(self.LocalLowPath):
            os.mkdir(self.LocalLowPath)
            firstTime = 1

        configSetup = open(f"{self.LocalLowPath}/config.json", "a")

        
        #Config Statuses
        self.settingsDict = {
            "titleBarStatus" : False
        }
        
        if firstTime == 1:
            # Serializing json
            json_object = dumps(self.settingsDict, indent=4)

            with open(f"{self.LocalLowPath}/config.json", "w") as config:
                config.write(json_object)
        
        #Status Variables
        self.running = False
        self.SettingsStatus = False


        #Creates Settings
        with open(f"{self.LocalLowPath}/config.json", "r") as config:
            configDict = load(config)

        self.settingsDict["titleBarStatus"] = configDict["titleBarStatus"]
        
        #Lists
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


        #Title Label
        self.AutoToolLabel = Label(self,text="PyAutoTool", width=40, height=1,bg=self.BackgroundColour,fg=self.ForegroundColour, font=(self.uiFont, 14),highlightbackground=self.BorderColour, highlightthickness=3)
        self.AutoToolLabel.place(x=8,y=5)
        
        #Creates Settings
        self.settingsIcon = Image.open("img/settings.png")
        self.settingsIcon = self.settingsIcon.resize((25,25),Image.LANCZOS)
        self.settingsIcon = ImageTk.PhotoImage(self.settingsIcon)

        self.Settings = Frame(self,bg=self.BackgroundColour,width=450,height=132,highlightthickness=3,highlightbackground=self.BorderColour,relief="solid")

        #Settings
        self.ToggleCustomTitleBarLabel = Label(self.Settings, text="Custom Titlebar(Janky):",bg=self.BackgroundColour,fg=self.ForegroundColour,font=(self.uiFont,12)).place(x=5,y=5)
        self.ToggleCustomTitleBarButton = Button(self.Settings, text="Off", bg=self.BackgroundColour, fg=self.ForegroundColour, font=(self.uiFont, 10),command=self.ToggleCustomTitleBar)
        self.ToggleCustomTitleBarButton.place(x=230, y=5)


        #Cretes frame for radio buttons
        self.optionsFrame = Frame(self, bg=self.BackgroundColour,width=120, height=132, highlightthickness=3, highlightbackground=self.BorderColour, relief="solid")
        self.optionsFrame.place(x=10, y=45)

        #Creates frame for showing errors
        self.errorFrame = Frame(self,bg=self.BackgroundColour,width=450, height=40, highlightthickness=3, highlightbackground=self.BorderColour, relief="solid")
        self.errorFrame.place(x=10, y=185)

        #Creates button for toggling settings
        self.settingsButton = Button(self.errorFrame,image=self.settingsIcon,bg=self.BackgroundColour,activebackground=self.BackgroundColour,borderwidth=0,command=self.openSettings)
        self.settingsButton.place(x=415,y=3)


        self.InitialOptions = StringVar()
        self.InitialOptions.set("Single Key")

        #Checks Settings
        self.setup()


        Radiobutton(self.optionsFrame, variable=self.InitialOptions,text="Single Key", value="Single Key", font=(self.uiFont, 10), bg=self.BackgroundColour,activebackground=self.BackgroundColour,fg=self.ForegroundColour, activeforeground=self.EntryColour,selectcolor=self.EntryColour, command=self.singlekeyFun).place(x=5, y=10)
        Radiobutton(self.optionsFrame, variable=self.InitialOptions,text="MultiKey", value="Multi Key",font=(self.uiFont, 10), bg=self.BackgroundColour,activebackground=self.BackgroundColour, activeforeground=self.EntryColour,fg=self.ForegroundColour,selectcolor=self.EntryColour, command=self.multikeyFun).place(x=5, y=50)
        Radiobutton(self.optionsFrame, variable=self.InitialOptions,text="Mouse", value="Mouse", font=(self.uiFont, 10), bg=self.BackgroundColour,activebackground=self.BackgroundColour, activeforeground=self.EntryColour,fg=self.ForegroundColour,selectcolor=self.EntryColour,command=self.mouseFun).place(x=5, y=90)

        

        

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
            self.HoldMouseLabel.place(x=130,y=32)
            self.HoldMouseLength.place(x=205,y=32)

        elif self.HoldMouse.get() == 0:
            self.HoldMouseLength.place_forget()
            self.HoldMouseLabel.place_forget()


    def __init__(self, keyInput = False, keyInputText = "", AutoEnter = False):
        #Gets arguments
        
        self.keyInput = bool(keyInput)
        self.keyInputText = keyInputText
        self.AutoEnter = AutoEnter
    
        #Creates variables
        self.AE = IntVar()
        self.MouseR = StringVar()
        self.MouseR.set("left")
        self.running = False

        #Construct Frame
        self.MyFrame = Frame(window, bg=window.BackgroundColour,width=320, height=132, padx=10, pady=10, highlightthickness=3, highlightbackground=window.BorderColour, relief="solid")
        self.MyFrame.place(x=140, y=45)

        # Delay
        Label(self.MyFrame, text="Enter Delay:",fg=window.ForegroundColour,font=(window.uiFont, 10,"underline"),bg=window.BackgroundColour).place(x=5,y=32)
        self.DelayEntry = Entry(self.MyFrame,fg=window.ForegroundColour,font=(window.uiFont, 10),bg=window.EntryColour,width=6,highlightcolor=window.BorderColour)
        self.DelayEntry.place(x=80, y=32)


        # Activation/Deactivation Key
        Label(self.MyFrame, text="Enter Toggle Key:", font=(window.uiFont, 10,"underline"),fg=window.ForegroundColour,bg=window.BackgroundColour).place(x=130, y=2)
        self.ADKeyEntry = Entry(self.MyFrame, font=(window.uiFont, 10),fg=window.ForegroundColour, bg=window.EntryColour,width=7,highlightcolor=window.BorderColour)
        self.ADKeyEntry.place(x=240,y=2)

        #Key Entry

        self.HoldMouse = IntVar()
        self.HoldMouse.set(0)

        if self.keyInput == True:
            self.KeyChoiseLabel = Label(self.MyFrame,font=(window.uiFont,10,"underline"), bg=window.BackgroundColour,fg=window.ForegroundColour)
            self.KeyChoiseEntry = Entry(self.MyFrame,font=(window.uiFont,10), bg=window.EntryColour,fg=window.ForegroundColour,width=7,highlightcolor=window.BorderColour)  
            if self.keyInputText == "Key":
                self.KeyChoiseLabel.configure(text="Enter key:")
            
            elif self.keyInputText == "Keys":
                self.KeyChoiseLabel.configure(text="Enter Keys:")
                
            self.KeyChoiseEntry.place(x=75,y=2)
            self.KeyChoiseLabel.place(x=5,y=2)

        elif self.keyInput == False:
            #Mouse Buttons
            Radiobutton(self.MyFrame, variable=self.MouseR,text="Left", value="left",bg=window.BackgroundColour, activeforeground=window.EntryColour, activebackground=window.BackgroundColour,selectcolor=window.EntryColour, fg=window.ForegroundColour).place(x=5, y=2)
            Radiobutton(self.MyFrame, variable=self.MouseR,text="Right", value="right",bg=window.BackgroundColour, activeforeground=window.EntryColour, activebackground=window.BackgroundColour,selectcolor=window.EntryColour, fg=window.ForegroundColour).place(x=55, y=2,)

            self.HoldMouseLabel = Label(self.MyFrame, text="Hold Time:", bg=window.BackgroundColour, fg=window.ForegroundColour,font=(window.uiFont, 10,"underline"))
            self.HoldMouseLength = Entry(self.MyFrame, bg=window.EntryColour, fg=window.ForegroundColour,width=14)

            
            self.HoldMouseButton=Checkbutton(self.MyFrame,  text="Hold",foreground=window.ForegroundColour,background=window.BackgroundColour,  variable=self.HoldMouse, selectcolor=window.EntryColour,activebackground=window.BackgroundColour,activeforeground=window.ForegroundColour,command=self.ToggleMouseHoldTime)
            self.HoldMouseButton.place(x=240, y=90)




        #Error Label
        self.ErrorLabel = Label(window.errorFrame, text="Remember: All units are in milliseconds. eg: 1000 = 1 second", bg=window.BackgroundColour, fg=window.ForegroundColour, font=(window.uiFont, 10))
        self.ErrorLabel.place(x=5,y=5)


        #Confirm Choise
        self.Confirm = Button(self.MyFrame, text="Confirm", command=self.start,height=1, bg=window.BackgroundColour, fg=window.ForegroundColour, activebackground=window.EntryColour, activeforeground=window.ForegroundColour)
        if self.running == False:
            self.Confirm.place(x=5, y=80)
        
        #Stop
        self.Stop = Button(self.MyFrame, text="Stop", command=lambda: [window.stop(), self.stopRunning() ],height=1, bg=window.BackgroundColour, fg=window.ForegroundColour, activebackground=window.EntryColour, activeforeground=window.ForegroundColour)
        if self.running == True:
            self.Stop.place(x=5, y=80)
    
        #Status Icon
        self.iconImageStopped = Image.open("img/statusStop.png")
        self.iconImageGo = Image.open("img/statusGo.png")
        self.iconImageGo = self.iconImageGo.resize((25,25), Image.LANCZOS)
        self.iconImageStopped = self.iconImageStopped.resize((25,25), Image.LANCZOS)
        
        if self.running == True:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageGo)
        
        elif self.running == False:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageStopped)
        
        self.imageStatusLabel = Label(self.MyFrame,image=self.iconImageTk, bg=window.BackgroundColour)
        self.imageStatusLabel.place(x=65,y=80)
    

        if self.AutoEnter == True:
            # AutoEnter
            Checkbutton(self.MyFrame, text="AE",foreground=window.ForegroundColour,background=window.BackgroundColour,  variable=self.AE, selectcolor=window.EntryColour,activebackground=window.BackgroundColour,activeforeground=window.ForegroundColour,command=self.updateAE).place(x=250,y=80)



    def updateRunning(self):
        if self.running == True:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageGo)
        
        elif self.running == False:
            self.iconImageTk = ImageTk.PhotoImage(self.iconImageStopped)

        self.imageStatusLabel.configure(image=self.iconImageTk)


    def start(self):
        #Error Detection
        keysString = ""
        if str(self.DelayEntry.get()).isdigit() != True:
            #Tell user to use an int
            self.ErrorLabel.configure(text="You must use a whole number")

        elif str(self.ADKeyEntry.get()) not in window.keys:
            self.ErrorLabel.configure(text="Please use key from list for activation key")

            for counter in window.keys:
                keysString += counter + ","

            keyWindow = Tk()
            keyWindow.title("List")
            keyWindow.attributes("-topmost",True)
            Label(keyWindow, text=keysString, wraplength=200).pack()

        elif self.keyInputText == "Key" and str(self.KeyChoiseEntry.get()) not in window.keys:
            self.ErrorLabel.configure(text="Please use key from list for autokey")

            for counter in window.keys:
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
            self.running = True
            self.updateRunning()

        #Removes error message
        self.ErrorLabel.configure(text="Remember: All units are in milliseconds. eg: 1000 = 1 second")

        #Toggles Confirm/Stop Button
        self.Stop.place(x=5, y=80)
        self.Confirm.place_forget()


    def stopRunning(self):
        self.running = False
        self.updateRunning()
        self.Confirm.place(x=5, y=80)
        self.Stop.place_forget()

window = App()
window.singlekeyFun()
window.mainloop()

# Serializing json
json_object = dumps(window.settingsDict, indent=4)

with open(f"{window.LocalLowPath}/config.json", "w") as config:
    config.write(json_object)
