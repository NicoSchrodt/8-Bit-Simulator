import sys

from PyQt6.QtWidgets import QApplication

from MainMenu import MainMenu


def main():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())


main()
