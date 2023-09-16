from json import dumps
from os import getlogin, mkdir

from requests import get


class Setup:
    def __init__(self) -> None:
        self.LocalLowPath = f"C:/Users/{getlogin()}/AppData/LocalLow/PyAutoTool"

    def firstTimeSetup(self) -> None:
        mkdir(self.LocalLowPath)
        self.downloadImages()
        self.setUpSettings()

    def downloadImages(self) -> None:
        mkdir(self.LocalLowPath + "/img")

        settings = get("https://github.com/AdamDunmore/PyAutoTool/blob/master/img/settings.png?raw=true")
        with open(self.LocalLowPath + '/img/settings.png', 'wb') as settingsImage:
            settingsImage.write(settings.content)

        statusGo = get("https://github.com/AdamDunmore/PyAutoTool/blob/master/img/statusGo.png?raw=true")
        with open(self.LocalLowPath + "/img/statusgo.png", 'wb') as statusGoImage:
            statusGoImage.write(statusGo.content)

        statusStop = get("https://github.com/AdamDunmore/PyAutoTool/blob/master/img/statusStop.png?raw=true")
        with open(self.LocalLowPath + "/img/statusstop.png", 'wb') as statusStopImage:
            statusStopImage.write(statusStop.content)   

    def setUpSettings(self) -> None:
        defaultSettings = {
            "titleBarStatus" : False,
            "alwaysOnTop" : True
        }

        # Serializing json
        json_object = dumps(defaultSettings, indent=4)

        with open(f"{self.LocalLowPath}/config.json", "w") as config:
            config.write(json_object)

