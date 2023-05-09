from PyQt6.QtCore import Qt, QThreadPool
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog
from MainWin.MainWinUse import *
import threading as th

from MainWin.MainWinUse import MainWindow
from PassWin.passWinD import *


class PassWin(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("Icons/login.png"))
        self.pushButton.setIcon(QIcon("Icons/ok.png"))
        self.pushButton_2.setIcon(QIcon("Icons/cancel.png"))
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.login)


    def cancel(self):
        self.close()

    def login(self):
        if self.lineEditPassword.text() == " " and self.lineEditUser.text() == "mundl":
            self.close()
            self.mainWin = MainWindow()





