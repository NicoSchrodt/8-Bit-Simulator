import os

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi


class ChangeValueWindow(QMainWindow):
    def __init__(self, Intel8080_MainWindow, btn):
        super(ChangeValueWindow, self).__init__(Intel8080_MainWindow)

        self.Intel8080_MainWindow = Intel8080_MainWindow
        self.btn = btn

        self.init_ui("ui\\ChangeValueWindow.ui")

        # Button definition
        button_ok = self.button_ok
        button_ok.clicked.connect(self.check_input)

        button_cancel = self.button_cancel
        button_cancel.clicked.connect(self.close)

        self.setWindowFlags(Qt.WindowType.Dialog)

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def check_input(self):
        try:
            value = int(self.lineEdit_value.text(), 16)
            index = self.btn.parent().parent().indexAt(self.btn.pos())
            if self.btn.parent().parent() == self.Intel8080_MainWindow.Registers_table:
                if 0 <= value < 256:  # May need to be different, depending on register
                    self.Intel8080_MainWindow.update_registers_table()
                    self.btn.parent().parent().cellWidget(index.row(), index.column()).setText(
                        self.lineEdit_value.text())
                    self.close()
            elif self.btn.parent().parent() == self.Intel8080_MainWindow.AdressLatch_table:
                if 0 <= value < 2:  # May need to be different, depending on register
                    self.Intel8080_MainWindow.update_adressLatch_table()
                    self.btn.parent().parent().cellWidget(index.row(), index.column()).setText(
                        self.lineEdit_value.text())
                    self.close()
        except Exception:
            pass
