import os.path

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

from Code.Intel8080.Intel8080_MainWindow import Intel8080_MainWindow
from Code.Tutorial.TutorialWindow import TutorialWindow


class MainMenu(QMainWindow):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.init_ui("ui\\MainMenu.ui")
        self.setWindowIcon(QIcon("../ui/Logo.png"))

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        # Intel8080 Button
        intel8080_button = self.button_Intel8080
        intel8080_button.clicked.connect(self.load_Intel8080)

        # Tutorial Button
        tutorial_button = self.button_Tutorial
        tutorial_button.clicked.connect(self.load_Tutorial)

        # Exit Button
        exit_button = self.button_Exit
        exit_button.clicked.connect(self.close)

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def load_Intel8080(self):
        self.hide()
        self.intel8080_window = Intel8080_MainWindow(self)
        self.intel8080_window.show()

    def load_Tutorial(self):
        self.hide()
        self.tutorial_window = TutorialWindow(self)
        self.tutorial_window.show()
