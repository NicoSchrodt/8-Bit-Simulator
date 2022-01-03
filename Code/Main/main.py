import sys

from PyQt6.QtWidgets import QApplication

from MainMenu import MainMenu
from Intel8080 import Intel8080


def main():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    a = Intel8080.Intel8080()
    sys.exit(app.exec())


main()
