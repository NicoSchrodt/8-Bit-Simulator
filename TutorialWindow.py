import os.path
import sys

from PyQt6.QtGui import QCloseEvent, QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi


def path(relativ):
    base_path = os.path.abspath("")
    full_path = os.path.join(base_path, relativ)
    return full_path


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class TutorialWindow(QMainWindow):
    def __init__(self, parent=None):
        super(TutorialWindow, self).__init__(None)
        self.mainW = parent
        self.init_ui(resource_path("Tutorial.ui"))
        self.setWindowIcon(QIcon(resource_path("Logo.png")))

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        # Menubar File
        Exit = self.actionExit
        Exit.triggered.connect(self.close)

        # Previous Button
        previous_button = self.previous_button
        previous_button.clicked.connect(self.previous)

        # Next Button
        next_button = self.next_button
        next_button.clicked.connect(self.next)

        self.page = 0
        self.names = ["Tutorial1.png", "Tutorial2.png", "Tutorial3.png", "Tutorial4.png", "Tutorial5.png"]

        self.Image.setPixmap(QPixmap(resource_path(self.names[self.page])))

    def init_ui(self, full_path):
        loadUi(full_path, self)

    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.mainW.show()
        # Closes Window and Un-Hides MainMenu

    def previous(self):
        if self.page != 0:
            self.page -= 1
            self.Image.setPixmap(QPixmap(resource_path(self.names[self.page])))

    def next(self):
        if self.page != 4:
            self.page += 1
            self.Image.setPixmap(QPixmap(resource_path(self.names[self.page])))
