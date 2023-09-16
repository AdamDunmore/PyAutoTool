import tkinter as tk

from theme import Theme
from widgets import Widgets

from json import dumps, load
from os import getlogin

theme = Theme()
widgets = Widgets()

class Settings(widgets.Frame):
    def __init__(self, master = None) -> None:
        super().__init__( master = master)
        self.configure(width=100, height=100)

        self.root = master.master

        self.fetchSettings()
        self.enforceSettings()

    def enforceSettings(self):
        if self.settingsDict["titleBarStatus"]:
            self.toggleCustomTitleBar()

        if self.settingsDict["alwaysOnTop"] == True:
            self.root.attributes("-topmost",True)


    def toggleSetting(self, setting):
        if setting == "titlebar":
            self.settingsDict["titleBarStatus"] = not self.settingsDict["titleBarStatus"]
            self.updateSettings()

            if self.settingsDict["titleBarStatus"] == True:
                self.titlebarButton.configure(text="On")

            else:
                self.titlebarButton.configure(text="Off")

            self.toggleCustomTitleBar()

        elif setting == "alwaysOnTop":
            self.settingsDict["alwaysOnTop"] = not self.settingsDict["alwaysOnTop"]
            self.updateSettings()

            if self.settingsDict["alwaysOnTop"] == True:
                self.alwaysOnTopButton.configure(text="On")
                self.root.attributes("-topmost",True)

            else:
                self.alwaysOnTopButton.configure(text="Off")
                self.root.attributes("-topmost",False)
                
    def createWidgets(self):
        titlebarLabel = widgets.Label(self, "Enable Custom Titlebar (Alpha)").grid(column=0,row=0, sticky=tk.W)
        self.titlebarButton = widgets.SettingsButton(master=self, text="Off", command=lambda: self.toggleSetting("titlebar"))
        self.titlebarButton.grid(column=1,row=0, sticky=tk.E)

        if self.settingsDict["titleBarStatus"] == True:
            self.titlebarButton.configure(text="On")

        alwaysOnTopLabel = widgets.Label(self, "Always on top").grid(column=0,row=1, sticky=tk.W)
        self.alwaysOnTopButton = widgets.SettingsButton(master=self, text="Off", command=lambda: self.toggleSetting("alwaysOnTop"))
        self.alwaysOnTopButton.grid(column=1,row=1, sticky=tk.E)

        if self.settingsDict["alwaysOnTop"] == True:
            self.alwaysOnTopButton.configure(text="On")



    def updateSettings(self):
        # Serializing json
        json_object = dumps(self.settingsDict, indent=4)

        with open(f"C:/Users/{getlogin()}/AppData/LocalLow/PyAutoTool/config.json", "w") as config:
            config.write(json_object)

        config.close()

    def fetchSettings(self):
        #Creates Settings
        with open(f"C:/Users/{getlogin()}/AppData/LocalLow/PyAutoTool/config.json", "r") as config:
            self.settingsDict = load(config)

        config.close()

    def toggleCustomTitleBar(self):
        if self.settingsDict["titleBarStatus"]:
            #Removes Windows title bar
            self.root.overrideredirect(True)

            #Increase Heigh
            self.root.geometry(f"{theme.geoWidth}x{int(theme.geoHeight) + 20}+0+0")

            self.titleBar = widgets.TitleBar(master=self.root)
            self.titleBar.pack(expand=1, fill=tk.X, side=tk.TOP,anchor=tk.N, pady=3)


            #Replace Settings
            self.root.settingsToggle.place_forget()
            self.root.settingsToggle.place(x=380, y=135)

        else:
            try:
                self.root.overrideredirect(False)

                #Increase Heigh
                self.root.geometry(f"{theme.geoWidth}x{theme.geoHeight}+0+0")

                self.titleBar.pack_forget()

                #Replace Settings
                self.root.settingsToggle.place_forget()
                self.root.settingsToggle.place(x=380, y=110)

            except:
                pass