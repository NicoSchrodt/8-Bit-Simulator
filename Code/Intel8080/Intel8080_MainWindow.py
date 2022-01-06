import os

from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class Intel8080_MainWindow(QMainWindow):
    def __init__(self):
        super(Intel8080_MainWindow, self).__init__()
        self.init_ui("ui\\Intel8080_MainWindow.ui")

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)
