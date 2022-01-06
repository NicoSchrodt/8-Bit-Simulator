import os

from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtGui import QCloseEvent


class Intel8080_MainWindow(QMainWindow):
    def __init__(self, parent):
        super(Intel8080_MainWindow, self).__init__(parent)
        self.init_ui("ui\\Intel8080_MainWindow.ui")

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def closeEvent(self, a0: QCloseEvent):
        self.close()
        self.parent().show()
        # Closes Window and Un-Hides MainMenu
