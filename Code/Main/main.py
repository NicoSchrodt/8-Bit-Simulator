import sys

from PyQt6.QtWidgets import QApplication

from MainMenu import MainMenu
from Code.Intel8080 import Intel8080


def main():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    processor = Intel8080.Intel8080()
    processor.run()
    sys.exit(app.exec())


main()
