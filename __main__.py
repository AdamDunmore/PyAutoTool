#Check Lists:
#   --Recordable Macros
#   --Themes (Ctk?)
#   --Implement CTK more
#   --Add Error Checking

#Fix List
#   --Add pip i requirements.txt

import eel
import eel.browsers
import os

from python.setup import Setup
from python.clicker import Keyboard_Clicker, Mouse_Clicker

setup = Setup()

mouse = Mouse_Clicker()
keyboard = Keyboard_Clicker()

@eel.expose
def Start_Mouse(data):
    mouse.Start(data)

@eel.expose
def Start_Keyboard(data):
    keyboard.Start(data)

def main():     
    #Preforms first time setup
    if not os.path.exists(setup.LocalLowPath):
       print("First time setup")
       setup.firstTimeSetup()
    #Starts web View
    eel.browsers.set_path('chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    eel.init('web')
    eel.start('index.html', size=(500, 250))

if __name__ == '__main__':
    main()

