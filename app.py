import tkinter as tk
import customtkinter as ctk
from PIL import Image

from modules import mouseMod, keyboardMod, browser, settings

from os import getlogin

from theme import Theme
from widgets import Widgets

theme = Theme()
widgets = Widgets()

class App(tk.Tk):
    def __init__(self) -> None:
        super(App,self).__init__() 
        self.configure(bg=theme.BackgroundColour)
        self.geometry(f"{theme.geoWidth}x{theme.geoHeight}+0+0")
        self.resizable(False,False)
        self.title("Autoclicker")


        self.settingsOn = False

        Main = widgets.Frame(master=self)
        Main.pack(fill=tk.X, padx=10, pady=10, anchor=tk.S, side=tk.BOTTOM)
        

        self.sidebar =  browser.Browser(master=Main)
        self.sidebar.pack(side=tk.LEFT ,padx=2, fill=tk.Y)

        self.mouse = mouseMod.Mouse(master = Main)
        self.keyboard = keyboardMod.Keyboard(master= Main)

        self.mouse.pack(side=tk.RIGHT ,padx=2, fill=tk.BOTH)

        #ctk.CTkImage = 
        settingsImage = ctk.CTkImage(light_image=Image.open(f"C:/Users/{getlogin()}/AppData/LocalLow/PyAutoTool/img/settings.png"))
        self.settingsToggle = ctk.CTkButton(master=self, width=1, height=1,fg_color=theme.BackgroundColour,hover_color=theme.BackgroundColour,image=settingsImage, command=self.toggleSettings)
        #self.settingsToggle = tk.Button(master=self, width=1, height=1, bg="red", command=self.toggleSettings)
        self.settingsToggle.place(x=380, y=110)

        self.Settings = settings.Settings(master=Main)

        self.Settings.createWidgets()

    def toggleSettings(self):
        if self.settingsOn:
            self.Settings.pack_forget()
            self.sidebar.MouseTab.config(state="normal")
            self.sidebar.KeyboardTab.config(state="normal")

            self.sidebar.MouseTab.config(relief="raised")
            self.sidebar.KeyboardTab.config(relief="raised")

        else:
            self.Settings.pack(side=tk.RIGHT ,padx=2, fill=tk.BOTH)  
            self.mouse.pack_forget()
            self.keyboard.pack_forget()

            self.sidebar.KeyboardTab.config(state="disabled")
            self.sidebar.MouseTab.config(state="disabled")

        self.settingsOn = not self.settingsOn
