import base64
from appmodule import BaseModule
import pyautogui


class ScreenShotModule(BaseModule):
    def run(self):
        im = pyautogui.screenshot()
        self.output = base64.b64encode(im.tobytes()).decode('utf-8')



def get_module():
    return ScreenShotModule