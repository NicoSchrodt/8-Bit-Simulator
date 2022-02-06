import os
import numpy as np

from time import sleep
from PyQt6 import QtCore
from PyQt6.QtCore import QObject, QThread
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt6.uic import loadUi
from PyQt6.QtGui import QCloseEvent, QIcon

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.ChangeValueWindow import ChangeValueWindow


class runThread(QObject):
    Source = QtCore.pyqtSignal()
    ExitFlag = False

    @QtCore.pyqtSlot()
    def monitor(self):
        while not self.ExitFlag:
            sleep(0.000001)  # Prevents freezing, may need fine-tuning
            self.Source.emit()


class Intel8080_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Intel8080_MainWindow, self).__init__(None)
        self.mainW = parent
        self.init_ui("ui\\Intel8080_MainWindow.ui")
        self.init_register_table()
        self.processor = Intel8080()
        self.processor.run()
        self.update_registers_table()

        # Thread Initialization
        self.monitor = None
        self.thread = None
        self.autorun = False
        self.init_thread()

        # Menubar File
        loadFile = self.actionLoad_Program
        loadFile.triggered.connect(self.load_program)

        # Next Instruction
        nextButton = self.next_button
        nextButton.pressed.connect(self.perform_instruction)

        # Go Instruction
        goButton = self.go_button
        goButton.pressed.connect(self.reset_go)

        # Address Latch
        addressLatch = self.AddressLatch_table
        addressLatch.setMaximumSize(self.getQTableWidgetSize(addressLatch))
        addressLatch.setMinimumSize(self.getQTableWidgetSize(addressLatch))

        for column in range(addressLatch.columnCount()):
            btn = QPushButton(addressLatch)
            btn.setText('{:x}'.format(0))
            addressLatch.setCellWidget(0, column, btn)
            btn.pressed.connect(self.pressed_table_cell)

        # Program Table
        Program_table = self.Program_table
        Program_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        self.setWindowTitle("Intel8080 Simulator")
        self.setWindowIcon(QIcon("../ui/Logo.png"))

    def getQTableWidgetSize(self, object):
        w = object.verticalHeader().width() + 2  # +2 seems to be needed
        for i in range(object.columnCount()):
            w += object.columnWidth(i)  # seems to include gridline (on my machine)
        h = object.horizontalHeader().height() + 2
        for i in range(object.rowCount()):
            h += object.rowHeight(i)
        return QtCore.QSize(w, h)

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def init_thread(self):
        self.monitor = runThread()
        self.thread = QThread(self)
        self.monitor.Source.connect(self.tasker_thread)
        self.monitor.moveToThread(self.thread)
        self.thread.started.connect(self.monitor.monitor)
        self.thread.start()

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
        # Registers_table.setMaximumSize(self.getQTableWidgetSize(Registers_table))
        # Registers_table.setMinimumSize(self.getQTableWidgetSize(Registers_table))

    def load_program(self):
        filepath = QFileDialog.getOpenFileName(self, 'Open file', os.path.dirname(os.path.realpath(__file__)), "*.com")
        if filepath[0] != "":
            self.processor.load_program(filepath[0])
            self.Program_table.setRowCount(0)  # Clear Table
            print(self.processor.program_length / 2)
            for i in range(int(self.processor.program_length / 2)):
                row = self.Program_table.rowCount()
                self.Program_table.insertRow(row)
                self.Program_table.setItem(row, 0, QTableWidgetItem(""))
                print(self.processor.program[i])
                self.Program_table.setItem(row, 1, QTableWidgetItem(hex(self.processor.program[i])
                                                                    + " " + hex(self.processor.program[i + 1])))
        self.reload_registers_table()

    def reset_go(self):
        self.autorun = not self.autorun

    def closeEvent(self, event: QCloseEvent):
        self.monitor.ExitFlag = True
        self.thread.quit()
        self.thread.wait()
        event.accept()
        self.mainW.show()
        # Closes Window and Un-Hides MainMenu

    @QtCore.pyqtSlot()
    def tasker_thread(self):
        if self.autorun:
            print("Performed Instruction, Automatic")
            self.processor.nextInstruction()
            self.reload_registers_table()

    def perform_instruction(self):
        if not self.autorun:
            self.processor.nextInstruction()
            self.reload_registers_table()

    def pressed_table_cell(self):
        btn = self.sender()
        self.dialog = ChangeValueWindow(self, btn)
        self.dialog.show()

    def reload_registers_table(self):  # This functions makes the ui match the registers
        Registers_table = self.Registers_table
        registers = self.processor.registers
        alu = self.processor.ALU
        Registers_table.cellWidget(0, 0).setText(str(registers.registers[0]))
        Registers_table.cellWidget(1, 0).setText(str(registers.registers[1]))
        Registers_table.cellWidget(2, 0).setText(str(registers.registers[9]))
        Registers_table.cellWidget(3, 0).setText(str(alu.temp_accumulator))
        Registers_table.cellWidget(4, 0).setText(str(registers.instruction_register))

    def update_registers_table(self):  # This function makes the registers match the ui
        Registers_table = self.Registers_table
        registers = self.processor.registers
        alu = self.processor.ALU
        # Registers_table.cellWidget(0, 0).setText('{:x}'.format(registers.registers[0]))  # PC
        registers.registers[0] = int(Registers_table.cellWidget(0, 0).text(), 16)
        # Registers_table.cellWidget(1, 0).setText('{:x}'.format(registers.registers[1]))  # SP
        registers.registers[1] = int(Registers_table.cellWidget(1, 0).text(), 16)
        # Registers_table.cellWidget(2, 0).setText('{:x}'.format(registers.registers[9]))  # ACC
        registers.registers[9] = int(Registers_table.cellWidget(2, 0).text(), 16)
        # Registers_table.cellWidget(3, 0).setText('{:x}'.format(alu.temp_accumulator))  # Temp-ACC
        alu.temp_accumulator = int(Registers_table.cellWidget(3, 0).text(), 16)
        # Registers_table.cellWidget(4, 0).setText('{:x}'.format(registers.instruction_register))  # INST
        registers.instruction_register = int(Registers_table.cellWidget(4, 0).text(), 16)

    def update_addressLatch_table(self):  # Technically an illegal operation, allowed for the purpose of the simulation
        AddressLatch_table = self.AddressLatch_table
        registers = self.processor.registers
        value = ""
        for i in range(16):
            value = value + str(int(AddressLatch_table.cellWidget(0, i).text()))
        value = int(value, 2)
        registers.address_latch = np.uint16(value)
        self.processor.peripherals.set_address_buffer(value)
