# install command: pyinstaller -p=C:\Users\Marko\anaconda3\envs\pyautogui\Lib\site-packages -F -w .\auto_hello_fun.py
from pyautogui import sleep
from auto_hello_gui import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import os, time
from PIL import Image, ImageQt
import numpy as np
import tkinter as tk
from screen_shot import ScreenShotGUI
import pyautogui as pg
SCREEN_H, SCREEN_W = 1440, 2560
SCREEN_SHOT_PATH = os.path.join(os.getcwd(), 'ScreenShot')

class AUTO_HELLO(Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        
        self.app = QtWidgets.QApplication(sys.argv)
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.target=None
        self.currentGreetNum = 0
        self.greetNum = 0
        self.pauseProgm = False
        self.printf('Welcome to AutoHello!')
        # Target Window Load Default Image
        default_path = os.path.join(SCREEN_SHOT_PATH, 'default.png')
        self.vizTargetWin(default_path)
        self.ScreenShotBtn.clicked.connect(self.ScreenShot)
        self.DefaultBtn.clicked.connect(lambda: self.vizTargetWin(default_path))
        self.StartBtn.clicked.connect(lambda: self.detectTarget(self.NumGreetSelect.value(), self.SpeedSelect.value()))
        self.PauseBtn.clicked.connect(self.stop)
        
        
    def ScreenShot(self):
        root = tk.Tk()
        ScreenShotGUI(root)
        root.mainloop()
        self.vizTargetWin(os.path.join(SCREEN_SHOT_PATH, 'image.png'))

    def vizTargetWin(self, path):
        img = Image.open(path).convert('RGBA')
        H, W, _ = np.array(img).shape    

        # DefaultImage = QtGui.QPixmap(path)
        DefaultImage = ImageQt.toqpixmap(img.transpose(Image.FLIP_LEFT_RIGHT))
        self.TargetWin.setGeometry(0, 0, H, W)
        self.TargetWin.setPixmap(DefaultImage)
        self.target = path

    def detectTarget(self, greetNum, speed, conf=0.8, ready_interval=5):
        self.pauseProgm = False
        self.greetNum = int(greetNum)
        if self.currentGreetNum >= self.greetNum:
            self.printf('ERROR! You have complete {} greetings. Input total number of greeting [{}] must be larger than that of current completion [{}].'\
                        .format(self.currentGreetNum, self.greetNum, self.currentGreetNum))
        self.start = time.time()
        # ready interval
        while ready_interval:
            if ready_interval == 1:
                clear_win = True
            else:
                clear_win = False
            self.printf('Start with {} second left'.format(ready_interval), clear_win)
            ready_interval -= 1
            time.sleep(1)
        
        while self.currentGreetNum < self.greetNum and not self.pauseProgm:
            icons = list(pg.locateAllOnScreen(self.target, confidence=conf))
            if len(icons) == 0:
                pg.scroll(-2000)
                self.printf('********* Process: [{}/{}] *********\n Can\'t find any targets.  Scroll the screen.'\
                        .format(self.currentGreetNum, self.greetNum), True)
                
            else:
                self.click_all_targets(icons, speed)
                

    def click_all_targets(self, icons, PAUSE=1.5):
        for icon in icons:
            if self.currentGreetNum == self.greetNum:
                duration = time.time() - self.start
                self.printf('********* Complete! *********\n  Sum of Detection: {};   Duration: {}'.format(self.currentGreetNum, duration), False)
                return None
            left, top, width, height = icon.left, icon.top, icon.width, icon.height
            center_x = left + width // 2
            center_y = top + height // 2
            # pg.moveTo(center_x, center_y, duration=1)
            pg.click(center_x, center_y, clicks=1)
            self.currentGreetNum += 1
            self.printf('********* Process: [{}/{}] *********\n Successfully detected and click.'\
                        .format(self.currentGreetNum, self.greetNum), True)
            if self.RandomSpeed.isChecked():
                pg.PAUSE = np.random.uniform(1, 3)
            else:
                pg.PAUSE = PAUSE
        return len(icons)
    
    def printf(self, mse, clear=False):
        self.Browser.append(mse)
        self.cursor = self.Browser.textCursor()
        self.Browser.moveCursor(self.cursor.End)
        QtWidgets.QApplication.processEvents()
        if clear:
            self.Browser.clear()

    def stop(self):
        self.pauseProgm = True
        self.printf('********* Program Interrupt! *********\n  Sum of Current Detection: {}.'.format(self.currentGreetNum), False)

if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    auto_hello = AUTO_HELLO()
    auto_hello.Form.show()
    sys.exit(auto_hello.app.exec_())