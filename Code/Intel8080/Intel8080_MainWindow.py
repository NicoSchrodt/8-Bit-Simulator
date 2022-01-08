import os

from PyQt6.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem
from PyQt6.uic import loadUi
from PyQt6.QtGui import QCloseEvent

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.ChangeValueWindow import ChangeValueWindow


class Intel8080_MainWindow(QMainWindow):
    def __init__(self, parent):
        super(Intel8080_MainWindow, self).__init__(parent)
        self.init_ui("ui\\Intel8080_MainWindow.ui")
        self.init_register_table()
        processor = Intel8080()
        #processor.run()

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def init_register_table(self):
        for row in range(self.Registers_table.rowCount()):
            print(row)
            btn = QPushButton(self.Registers_table)
            btn.setText('{:x}'.format(0))
            self.Registers_table.setCellWidget(row, 0, btn)
            btn.pressed.connect(self.pressed_table_cell)

    def closeEvent(self, a0: QCloseEvent):
        print("Test")
        self.close()
        self.parent().show()
        # Closes Window and Un-Hides MainMenu

    def pressed_table_cell(self):
        btn = self.sender()
        self.dialog = ChangeValueWindow(self, btn)
        self.dialog.show()

    def update_registers_table(self):
        # To be implemented
        pass
