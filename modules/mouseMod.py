import tkinter as tk
import mouse
import keyboard

from theme import Theme
from widgets import Widgets

theme = Theme()
widgets = Widgets()

class Mouse(widgets.Frame):
    def __init__(self, master = None) -> None:
        super(Mouse,self).__init__(master=master)
        self.Status = False
        self.Running = False
       
        self.createWidgets()
        
    def createWidgets(self) -> None:
        # Delay
        self.DelayEntry = widgets.Entry(master=self, placeholder_text="Enter Delay")
        self.DelayEntry.grid(column=0, row=0, columnspan = 2)

        # Activation/Deactivation Key
        self.ADKeyEntry = widgets.Entry(master=self, placeholder_text="Enter Toggle Key")
        self.ADKeyEntry.grid(column=0, row=1, columnspan = 2)

        #Mouse Buttons
        self.MouseButtonEntry = tk.StringVar()
        self.MouseButtonEntry.set("left")

        widgets.Radio(master = self, text="Left", value="left", variable=self.MouseButtonEntry).grid(column=0, row=2)
        widgets.Radio(master = self,text="Right", value="right" , variable=self.MouseButtonEntry).grid(column=1, row=2) 

        #Start/Stop
        self.StartButton = widgets.Start(master=self, command=self.Start, text="Start")
        self.StartButton.grid(column=0,row=3)



    def getWidgetInfo(self) -> None:
        self.Delay = int(self.DelayEntry.get())
        self.ActivationButton = self.ADKeyEntry.get()
        self.MouseButton = self.MouseButtonEntry.get()

    def Toggle(self) -> None:
        self.Running = not self.Running

    def Start(self) -> None:
        if self.Status == False:
            self.getWidgetInfo()
            self.StartButton.configure(text="Stop")
            self.Status = not self.Status
            keyboard.add_hotkey(self.ActivationButton, self.Toggle)

            
            self.after((self.Delay * 1000), self.Event)

        elif self.Status == True:
            self.StartButton.configure(text="Start")
            self.Status = not self.Status
            self.Running = False
            keyboard.remove_all_hotkeys()
  
    def Event(self) -> None:
        if self.Running == True:
            mouse.click(self.MouseButton)
        if self.Status == True:
            self.after((self.Delay * 1000), self.Event)

    