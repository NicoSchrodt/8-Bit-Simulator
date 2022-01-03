import os.path

from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi


class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.init_ui("ui\\MainMenu.ui")

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        print(full_path)
        loadUi(full_path, self)

    def load_Intel8080(self):
        pass

    def load_Tutorial(self):
        pass

    def exit_program(self):
        pass
