import os

from PyQt6.QtGui import QIcon
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

        self.setWindowIcon(QIcon("../ui/Logo.png"))
        try:
            index = self.btn.parent().parent().indexAt(self.btn.pos())
            if self.btn.parent().parent() == self.Intel8080_MainWindow.Registers_table:
                self.setWindowTitle(self.btn.parent().parent().verticalHeaderItem(index.row()).text())
            else:
                self.setWindowTitle("Change Value")
        except:
            pass

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def check_input(self):
        try:
            value = int(self.lineEdit_value.text(), 16)
            index = self.btn.parent().parent().indexAt(self.btn.pos())
            if self.btn.parent().parent() == self.Intel8080_MainWindow.Registers_table:
                # self.setWindowTitle(self.)
                if 0 <= value < 256:  # May need to be different, depending on register
                    self.btn.parent().parent().cellWidget(index.row(), index.column()).setText(
                        self.lineEdit_value.text())
                    self.Intel8080_MainWindow.update_registers_table()
                    self.close()
            elif self.btn.parent().parent() == self.Intel8080_MainWindow.Register_array_table:
                if 0 <= value < 256:  # May need to be different, depending on register
                    self.btn.parent().parent().cellWidget(index.row(), index.column()).setText(
                        self.lineEdit_value.text())
                    self.Intel8080_MainWindow.update_register_array_table()
                    self.close()
            elif self.btn.parent().parent() == self.Intel8080_MainWindow.ProgramMemory_table:
                if 0 <= value < 256:
                    self.btn.parent().parent().cellWidget(index.row(), index.column()).setText(
                        self.lineEdit_value.text())
                    self.Intel8080_MainWindow.update_memory_table()
                    self.close()
        except Exception as e:
            pass
