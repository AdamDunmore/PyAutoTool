#Check Lists:
#   --Recordable Macros
#   --Themes (Ctk?)
#   --Implement CTK more
#   --Add Error Checking

import os
import tkinter as tk

from app import App
from setup import Setup

from theme import Theme

setup = Setup()
theme = Theme()

if __name__ == "__main__":
    if not os.path.exists(setup.LocalLowPath):
        print("First time setup")
        setup.firstTimeSetup()

    app = App()

    tk.mainloop()

