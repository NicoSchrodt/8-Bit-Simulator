import os.path

from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from Code.Intel8080.Intel8080_MainWindow import Intel8080_MainWindow

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.init_ui("ui\\MainMenu.ui")

        # Intel8080 Button
        intel8080_button = self.button_Intel8080
        intel8080_button.pressed.connect(self.load_Intel8080)

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        print(full_path)
        loadUi(full_path, self)

    def load_Intel8080(self):
        self.dialog = Intel8080_MainWindow()
        self.dialog.show()

    def load_Tutorial(self):
        pass

    def exit_program(self):
        pass
