import tkinter as tk
import keyboard

from theme import Theme
from widgets import Widgets

theme = Theme()
widgets = Widgets()

class Keyboard(widgets.Frame):
    def __init__(self, master = None) -> None:
        super(Keyboard, self).__init__(master=master)
        self.Status = False
        self.Running = False

        self.createWidgets()

    def createWidgets(self) -> None:
        # Delay
        self.DelayEntry = widgets.Entry(master=self, placeholder_text="Enter Delay")
        self.DelayEntry.grid(column=0, row=0, columnspan=2)

        # Activation/Deactivation Key
        self.ADKeyEntry = widgets.Entry(master=self, placeholder_text="Enter Toggle Key")
        self.ADKeyEntry.grid(column=0, row=1, columnspan=2)

        #Keyboard Key
#Enable string.length checking
        self.KeyEntry = widgets.Entry(master=self, placeholder_text="Enter Key to Press")
        self.KeyEntry.grid(column=0, row=2, columnspan=2)

        #Start/Stop
        self.StartButton = widgets.Start(master=self, command=self.Start, text="Start")
        self.StartButton.grid(column=0,row=3)

    def getWidgetInfo(self) -> None:
        self.Delay = int(self.DelayEntry.get())
        self.ActivationButton = self.ADKeyEntry.get()
        self.KeyButton = self.KeyEntry.get()

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
            keyboard.press_and_release(self.KeyButton)
        if self.Status == True:
            self.after((self.Delay * 1000), self.Event)