import tkinter as tk

from theme import Theme
from widgets import Widgets

from modules import mouseMod, keyboardMod

theme = Theme()
widgets = Widgets()


class Browser(tk.Frame):
    def __init__(self, master = None, highlightthickness = 3, highlightbackground=theme.BorderColour,bg=theme.BackgroundColour) -> None:
        super().__init__(master,highlightthickness=highlightthickness, highlightbackground=highlightbackground,bg=bg)
        self.root = master.master

        self.tab = "Mouse"

        self.MouseTab = widgets.Tab(master=self, text="Mouse", command=lambda: self.changeTab("Mouse"), relief="sunken")
        self.MouseTab.config(state="disabled")
        self.MouseTab.pack(pady=3, padx=3, fill=tk.BOTH)
        self.KeyboardTab = widgets.Tab(master=self, text="Keyboard", command=lambda: self.changeTab("Keyboard"))
        self.KeyboardTab.pack(pady=3, padx=3, fill=tk.BOTH)

    def changeTab(self, tab) -> None:
        self.tab = tab
        if self.tab == "Mouse":
            self.root.keyboard.pack_forget()
            self.root.mouse.pack(side=tk.RIGHT ,padx=2, fill=tk.BOTH)

            self.MouseTab.configure(relief="sunken")
            self.KeyboardTab.configure(relief="raised")

            self.MouseTab.config(state="disabled")
            self.KeyboardTab.config(state="normal")

        elif self.tab == "Keyboard":
            self.root.mouse.pack_forget()
            self.root.keyboard.pack(side=tk.RIGHT ,padx=2, fill=tk.BOTH)

            self.KeyboardTab.configure(relief="sunken")
            self.MouseTab.configure(relief="raised")

            self.KeyboardTab.config(state="disabled")
            self.MouseTab.config(state="normal")