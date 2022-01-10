import os

from PyQt6.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem, QHeaderView
from PyQt6.uic import loadUi
from PyQt6.QtGui import QCloseEvent

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.ChangeValueWindow import ChangeValueWindow


class Intel8080_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Intel8080_MainWindow, self).__init__(None)
        self.mainW = parent
        self.init_ui("ui\\Intel8080_MainWindow.ui")
        self.init_register_table()
        self.processor = Intel8080()
        # processor.run()
        self.update_registers_table()

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def init_register_table(self):
        Registers_table = self.Registers_table
        # Registers_table.horizontalHeader().setVisible(False)
        # Registers_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        # Done in QT-Designer
        for row in range(Registers_table.rowCount()):
            btn = QPushButton(Registers_table)
            btn.setText('{:x}'.format(0))
            Registers_table.setCellWidget(row, 0, btn)
            btn.pressed.connect(self.pressed_table_cell)

    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.mainW.show()
        # Closes Window and Un-Hides MainMenu

    def pressed_table_cell(self):
        btn = self.sender()
        self.dialog = ChangeValueWindow(self, btn)
        self.dialog.show()

    def update_registers_table(self):
        Registers_table = self.Registers_table
        registers = self.processor.registers
        alu = self.processor.ALU
        #Registers_table.cellWidget(0, 0).setText('{:x}'.format(registers.registers[0]))  # PC
        registers.registers[0] = int(Registers_table.cellWidget(0, 0).text(), 16)
        #Registers_table.cellWidget(1, 0).setText('{:x}'.format(registers.registers[1]))  # SP
        registers.registers[1] = int(Registers_table.cellWidget(1, 0).text(), 16)
        #Registers_table.cellWidget(2, 0).setText('{:x}'.format(registers.registers[9]))  # ACC
        registers.registers[9] = int(Registers_table.cellWidget(2, 0).text(), 16)
        #Registers_table.cellWidget(3, 0).setText('{:x}'.format(alu.temp_accumulator))  # Temp-ACC
        alu.temp_accumulator = int(Registers_table.cellWidget(3, 0).text(), 16)
        #Registers_table.cellWidget(4, 0).setText('{:x}'.format(registers.instruction_register))  # INST
        registers.instruction_register = int(Registers_table.cellWidget(4, 0).text(), 16)
