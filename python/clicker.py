from time import sleep
import keyboard
import mouse
import threading

class Clicker_Base:
    def __init__(self) -> None:
        self.running = False
        self.pressing = False
        
    def Toggle(self) -> None:
        self.running = not self.running
        if self.running == False:
            self.pressing = False
            keyboard.unhook_all_hotkeys()
        else:
            keyboard.add_hotkey(self.data["toggle_key"], self.Toggle_Pressing)

    def Toggle_Pressing(self) -> None:
        self.pressing = not self.pressing

    def Event(self):
        #Super function in child class
        pass

    def Event_Loop(self):
        while self.running:
            if self.pressing:
                self.Event()
                sleep(float(self.data["delay"]))

    def Start(self, data):
        self.data = data
        self.Toggle()
        event_thread = threading.Thread(target=self.Event_Loop)
        event_thread.start()

class Mouse_Clicker(Clicker_Base):
    def Event(self):
        mouse.click(self.data["pressing_key"])

class Keyboard_Clicker(Clicker_Base):
    def Event(self):
        keyboard.press(self.data["pressing_key"])
        keyboard.release(self.data["pressing_key"])