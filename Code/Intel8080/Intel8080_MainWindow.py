import os

from time import sleep
from PyQt6 import QtCore
from PyQt6.QtCore import QObject, QThread
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt6.uic import loadUi
from PyQt6.QtGui import QCloseEvent, QIcon, QColor

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.ChangeValueWindow import ChangeValueWindow
from Code.Intel8080.StateLogger import StateLogger


class runThread(QObject):
    Source = QtCore.pyqtSignal()
    ExitFlag = False

    @QtCore.pyqtSlot()
    def monitor(self):
        while not self.ExitFlag:
            sleep(0.1)  # Prevents freezing, may need fine-tuning
            self.Source.emit()


command_dict = {
    0xCE: [1, "ACI"],  # ACI
    0x88: [0, "ADC"],  # ADC BIT 0-2 REG --> 0xF8
    0x80: [0, "ADD"],  # ADD BIT 0-2 REG --> 0xF8
    0xC6: [1, "ADI"],  # ADI
    0xA0: [0, "ANA"],  # ANA BIT 0-2 REG --> 0xF8
    0xE6: [1, "ANI"],  # ANI
    0xCD: [2, "CALL"],  # CALL
    0xDC: [2, "CALL CC"],  # CALL CC
    0xFC: [2, "CALL CM"],  # CALL CM
    0x2F: [0, "CMA"],  # CMA
    0x3F: [0, "CMC"],  # CMC
    0xB8: [0, "CMP"],  # CMP BIT 0-2 REG --> 0xF8
    0xD4: [2, "CALL CNC"],  # CALL CNC
    0xC4: [2, "CALL CNZ"],  # CALL CNZ
    0xF4: [2, "CALL CP"],  # CALL CP
    0xEC: [2, "CALL CPE"],  # CALL CPE
    0xFE: [1, "CPI"],  # CPI
    0xE4: [2, "CALL CPO"],  # CALL CPO
    0xCC: [2, "CALL CZ"],  # CALL CZ
    0x27: [0, "DAA"],  # DAA
    0x09: [0, "DAD"],  # DAD BIT 4-5 OP --> 0xCF
    0x05: [0, "DCR"],  # DCR BIT 3-5 REG --> 0xC7
    0x0B: [0, "DCX"],  # DCX BIT 4-5 OP --> 0xCF
    0xF3: [0, "DI"],  # DI
    0xFB: [0, "EI"],  # EI
    0x76: [0, "HLT"],  # HLT
    0xDB: [1, "IN"],  # IN
    0x04: [0, "INR"],  # INR BIT 3-5 REG --> 0xC7
    0x03: [0, "INX"],  # INX BIT 4-5 OP --> 0xCF
    0xDA: [2, "JC"],  # JC
    0xFA: [2, "JM"],  # JM
    0xC3: [2, "JMP"],  # JMP
    0xD2: [2, "JNC"],  # JNC
    0xC2: [2, "JNZ"],  # JNZ
    0xF2: [2, "JP"],  # JP
    0xEA: [2, "JPE"],  # JPE
    0xE2: [2, "JPO"],  # JPO
    0xCA: [2, "JZ"],  # JZ
    0x3A: [2, "LDA"],  # LDA
    0x0A: [0, "LDAX B"],  # LDAX_B
    0x1A: [0, " LDAX D"],  # LDAX_D
    0x2A: [2, "LHLD"],  # LHLD
    0x01: [2, "LXI"],  # LXI BIT 4-5 REG --> 0xCF
    0x40: [0, "MOV"],  # MOV BIT 0-2, 3-5 OP --> 0xC0
    0x06: [1, "MVI"],  # MVI BIT 3-5 DATA --> 0xC7
    0x00: [0, "NOP"],  # NOP
    0xB0: [0, "ORA"],  # ORA BIT 0-2 REG --> 0xF8
    0xF6: [1, "ORI"],  # ORI
    0xD3: [1, "OUT"],  # OUT
    0xE9: [0, "PCHL"],  # PCHL
    0xC1: [0, "POP"],  # POP BIT 4-5 OP --> 0xCF
    0xC5: [0, "PUSH"],  # PUSH BIT 4-5 OP --> 0xCF
    0x17: [0, "RAL"],  # RAL
    0x1F: [0, "RAR"],  # RAR
    0xD8: [0, "RC"],  # RC
    0xC9: [0, "RET"],  # RET
    0x07: [0, "RLC"],  # RLC
    0xF8: [0, "RM"],  # RM
    0xD0: [0, "RNC"],  # RNC
    0xC0: [0, "RNZ"],  # RNZ
    0xF0: [0, "RP"],  # RP
    0xE8: [0, "RPE"],  # RPE
    0x70: [0, "RPO"],  # RPO
    0x0F: [0, "RRC"],  # RRC
    0xC7: [0, "RST"],  # RST BIT 3-5 OP --> 0xC7
    0xC8: [0, "RZ"],  # RZ
    0x98: [0, "SBB"],  # SBB BIT 0-2 REG --> 0xF8
    0xDE: [1, "SBI"],  # SBI
    0x22: [2, "SHLD"],  # SHLD
    0xF9: [0, "SPHL"],  # SPHL
    0x32: [2, "STA"],  # STA
    0x02: [0, "STAX B"],  # STAX_B
    0x12: [0, "STAX D"],  # STAX_D
    0x37: [0, "STC"],  # STC
    0x90: [0, "SUB"],  # SUB BIT 1-3 REG --> 0xF8
    0xD6: [1, "SUI"],  # SUI
    0xEB: [0, "XCHG"],  # XCHG
    0xA8: [0, "XRA"],  # XRA BIT 0-2 REG --> 0xF8
    0xEE: [1, "XRI"],  # XRI
    0xE3: [0, "XTHL"],  # XTHL
}

command_masks = [0xFF, 0xF8, 0xCF, 0xC7, 0xC0]


class Intel8080_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Intel8080_MainWindow, self).__init__(None)
        self.mainW = parent
        self.init_ui("ui\\Intel8080_MainWindow.ui")
        self.init_register_table()
        self.init_register_array_table()
        self.Logger = StateLogger(self.MessageLog_plaintext)
        self.processor = Intel8080(parent_window=None, logger=self.Logger)
        self.Logger.addEntry("Welcome :)")
        # self.processor.run()

        # Thread Initialization
        self.monitor = None
        self.thread = None
        self.autorun = False
        self.init_thread()

        # Menubar File
        loadFile = self.actionLoad_Program
        loadFile.triggered.connect(self.load_program)

        # Next Instruction/MachineCycle/State
        self.next_button.pressed.connect(self.perform_instruction)
        self.next_mc_button.pressed.connect(self.perform_mc)
        self.next_state_button.pressed.connect(self.perform_state)

        # Go Instruction
        goButton = self.go_button
        goButton.pressed.connect(self.reset_go)

        # Reset Instruction
        resetButton = self.reset_button
        resetButton.pressed.connect(self.reset_intel8080)

        # Cycle State Table #ToDo: Fix this horrible mess (at least it looks proper now)
        CycleStateTable = self.CycleState_table
        qz = self.getQTableWidgetSize(CycleStateTable)
        qz.setWidth(qz.width() + 38)
        qz.setHeight(qz.height() - 24)
        CycleStateTable.setMaximumSize(qz)
        # CycleStateTable.setMinimumSize(qz)
        #CycleStateTable.resizeColumnsToContents()

        # Program Memory Table
        for row in range(self.ProgramMemory_table.rowCount()):
            for column in range(self.ProgramMemory_table.columnCount()):
                btn = QPushButton(self.ProgramMemory_table)
                btn.setText('{:x}'.format(0))
                self.ProgramMemory_table.setCellWidget(row, column, btn)
                btn.pressed.connect(self.pressed_table_cell)
        # self.ProgramMemory_table.resizeColumnsToContents()

        # Program Memory Range
        self.From_sb.valueChanged.connect(self.adjust_to)
        self.To_sb.valueChanged.connect(self.adjust_from)
        self.lock = False
        self.Display_button.pressed.connect(self.reload_memory_table)

        # Program Table
        Program_table = self.Program_table
        Program_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        Program_table.cellClicked.connect(self.breakpoint_check)

        self.instruction_positions = []
        self.previous_pc = 0

        self.setWindowTitle("Intel8080 Simulator")
        self.setWindowIcon(QIcon("../ui/Logo.png"))

        self.update_ui()

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

    def init_register_array_table(self):
        Register_array_table = self.Register_array_table
        for row in range(Register_array_table.rowCount()):
            for column in range(Register_array_table.columnCount()):
                btn = QPushButton(Register_array_table)
                btn.setText('{:x}'.format(0))
                Register_array_table.setCellWidget(row, column, btn)
                btn.pressed.connect(self.pressed_table_cell)

    def load_program(self):
        filepath = QFileDialog.getOpenFileName(self, 'Open file', os.path.dirname(os.path.realpath(__file__)), "*.com")
        if filepath[0] != "":
            self.reset_intel8080()
            self.processor.load_program(filepath[0])
            self.fill_program_table()
        self.update_ui()

    def adjust_to(self, value):
        if self.lock is False:
            self.lock = True
            if value % 16 != 0:
                self.From_sb.setValue(value - (value % 16))
                self.To_sb.setValue(value + 128 - (value % 16))
            else:
                self.To_sb.setValue(value + 128)
            self.lock = False

    def adjust_from(self, value):
        if self.lock is False:
            self.lock = True
            if value < 128:
                value = 128
            if value % 16 != 0:
                self.To_sb.setValue(value - (value % 16))
                self.From_sb.setValue(value - 128 - (value % 16))
                self.lock = False
            else:
                self.From_sb.setValue(value - 128)
            self.lock = False

    def reload_program(self):
        self.fill_program_table()
        self.update_ui()

    def reset_go(self):
        self.autorun = not self.autorun

    def reset_intel8080(self):
        self.processor.reset_processor()
        self.update_ui()

    def update_ui(self):
        self.fill_program_table()
        self.color_program_table()
        self.color_cycle_state()
        self.reload_memory_table()
        self.reload_registers_table()
        self.reload_register_array_table()

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
            self.processor.next_instruction()
            self.update_ui()

    def perform_instruction(self):
        if self.actionCheck():
            self.processor.next_instruction()
            self.update_ui()

    def perform_mc(self):
        if self.actionCheck():
            self.processor.next_machine_cycle()
            self.update_ui()

    def perform_state(self):
        if self.actionCheck():
            self.processor.next_state()
            self.update_ui()

    def sendInterrupt(self):
        if self.actionCheck():
            try:
                value = int(self.Interrupt_line.text())
            except:
                self.Logger.addEntry("Invalid Interrupt Sent")
            else:
                if (0 <= value) and (value <= 255):
                    self.processor.interrupted = True
                    self.processor.interrupt_instruction = value
                else:
                    self.Logger.addEntry("Invalid Interrupt Byte")

    def actionCheck(self):
        return not self.autorun

    def pressed_table_cell(self):
        btn = self.sender()
        self.dialog = ChangeValueWindow(self, btn)
        self.dialog.show()

    def breakpoint_check(self, row, column):
        if column == 0:
            if self.Program_table.item(row, column) is None:
                self.Program_table.setItem(row, column, QTableWidgetItem("B"))
            elif self.Program_table.item(row, column).text() != "B":
                self.Program_table.setItem(row, column, QTableWidgetItem("B"))
            else:
                self.Program_table.setItem(row, column, QTableWidgetItem(""))

    def fill_program_table(self):
        self.instruction_positions = []
        self.Program_table.setRowCount(0)  # Clear Table
        try:
            i = 0
            nop_counter = 0
            while i < pow(2, 16):
                if nop_counter < 1:
                    self.instruction_positions.append(i)
                for j in range(len(command_masks)):
                    masked_command = self.processor.program[i] & command_masks[j]
                    if masked_command in command_dict:
                        if masked_command == 0x00:
                            nop_counter += 1
                        else:
                            nop_counter = 0
                        if not (nop_counter > 1):
                            operands = command_dict[masked_command][0]
                            row = self.Program_table.rowCount()
                            self.Program_table.insertRow(row)
                            self.Program_table.setItem(row, 0, QTableWidgetItem(""))
                            itemtext = str(i)
                            itemtext = itemtext + " " + command_dict[masked_command][1]
                            itemtext = itemtext + " " + hex(self.processor.program[i])
                            for k in range(i, i + operands):
                                itemtext = itemtext + " " + hex(self.processor.program[k + 1])
                            self.Program_table.setItem(row, 1, QTableWidgetItem(itemtext))
                            break
                i += operands + 1
        except Exception as e:
            print("ERROR: " + str(e))

    def color_cycle_state(self):
        CurrentMachineCycle = self.processor.current_machine_cycle - 1
        CurrentState = self.processor.current_instruction.machine_cycles[self.processor.current_machine_cycle - 1].last_executed_state
        CST = self.CycleState_table
        # ToDo: Technically Wrong, doesn't differentiate what Machine cycle it is
        for i in range(5):
            CST.item(0, i).setBackground(QColor(255, 255, 255))
        CST.item(0, CurrentMachineCycle).setBackground(QColor(152, 245, 255))
        for i in range(5):
            CST.item(1, i).setBackground(QColor(255, 255, 255))
        CST.item(1, CurrentState).setBackground(QColor(152, 245, 255))

    def color_program_table(self):
        try:
            index = -1
            current_pc = self.processor.get_pc()
            while index == -1:
                if current_pc in self.instruction_positions:
                    index = self.instruction_positions.index(current_pc)
                else:
                    current_pc -= 1
            if index != 0:
                self.Program_table.item(self.instruction_positions.index(index) - 1, 0).setBackground(QColor(255, 255, 255))
                self.Program_table.item(self.instruction_positions.index(index) - 1, 1).setBackground(QColor(255, 255, 255))
            self.Program_table.item(self.instruction_positions.index(index), 0).setBackground(QColor(152, 245, 255))
            self.Program_table.item(self.instruction_positions.index(index), 1).setBackground(QColor(152, 245, 255))
        except Exception as e:
            print("Exception" + str(e))
        return

    def reload_registers_table(self):  # This functions makes the ui match the registers
        Processor = self.processor
        Registers_table = self.Registers_table

        Registers_table.cellWidget(0, 0).setText(str(Processor.get_pc()))  # PC
        Registers_table.cellWidget(1, 0).setText(str(Processor.get_sp()))  # SP
        Registers_table.cellWidget(2, 0).setText(str(Processor.get_acc()))  # ACC
        Registers_table.cellWidget(3, 0).setText(str(Processor.get_act()))  # Temp-ACC
        Registers_table.cellWidget(4, 0).setText(str(Processor.get_instruction_reg()))  # INST

    def update_registers_table(self):  # This function makes the registers match the ui
        Processor = self.processor
        Registers_table = self.Registers_table
        Processor.set_pc(int(Registers_table.cellWidget(0, 0).text(), 16))  # PC
        Processor.set_sp(int(Registers_table.cellWidget(1, 0).text(), 16))  # SP
        Processor.set_acc(int(Registers_table.cellWidget(2, 0).text(), 16))  # ACC
        Processor.set_act(int(Registers_table.cellWidget(3, 0).text(), 16))  # Temp-ACC
        Processor.set_instruction_reg(int(Registers_table.cellWidget(4, 0).text(), 16))  # INST

    def reload_register_array_table(self):
        Processor = self.processor
        Register_array_table = self.Register_array_table

        Register_array_table.cellWidget(0, 0).setText(str(Processor.get_reg_array_direct('w')))
        Register_array_table.cellWidget(0, 1).setText(str(Processor.get_reg_array_direct('z')))
        Register_array_table.cellWidget(1, 0).setText(str(Processor.get_reg_array_direct('b')))
        Register_array_table.cellWidget(1, 1).setText(str(Processor.get_reg_array_direct('c')))
        Register_array_table.cellWidget(2, 0).setText(str(Processor.get_reg_array_direct('d')))
        Register_array_table.cellWidget(2, 1).setText(str(Processor.get_reg_array_direct('e')))
        Register_array_table.cellWidget(3, 0).setText(str(Processor.get_reg_array_direct('h')))
        Register_array_table.cellWidget(3, 1).setText(str(Processor.get_reg_array_direct('l')))

    def update_register_array_table(self):
        Processor = self.processor
        Register_array_table = self.Register_array_table
        Processor.set_reg_array_direct('w', int(Register_array_table.cellWidget(0, 0).text(), 16))
        Processor.set_reg_array_direct('z', int(Register_array_table.cellWidget(0, 1).text(), 16))
        Processor.set_reg_array_direct('b', int(Register_array_table.cellWidget(1, 0).text(), 16))
        Processor.set_reg_array_direct('c', int(Register_array_table.cellWidget(1, 1).text(), 16))
        Processor.set_reg_array_direct('d', int(Register_array_table.cellWidget(2, 0).text(), 16))
        Processor.set_reg_array_direct('e', int(Register_array_table.cellWidget(2, 1).text(), 16))
        Processor.set_reg_array_direct('h', int(Register_array_table.cellWidget(3, 0).text(), 16))
        Processor.set_reg_array_direct('l', int(Register_array_table.cellWidget(3, 1).text(), 16))

    def reload_memory_table(self):  # make ui match the program memory
        Startvalue = self.From_sb.value()
        for i in range(8):
            for j in range(16):
                address = Startvalue + i * 16 + j  # one rows = 16 bits, one column 1 bit
                value = str(hex(self.processor.get_memory_byte(address))).replace('0x', '')
                self.ProgramMemory_table.cellWidget(i, j).setText(str(value))
        values = []
        for i in range(Startvalue, Startvalue + 144, 16):
            values.append(hex(i))
        self.ProgramMemory_table.setVerticalHeaderLabels(values)

    def update_memory_table(self):  # make program memory match the ui
        Startvalue = self.From_sb.value()
        for i in range(8):
            for j in range(16):
                address = Startvalue + i * 16 + j  # one row = 16 bits, one column 1 bit
                value = int(self.ProgramMemory_table.cellWidget(i, j).text(), 16)
                self.processor.set_memory_byte(address, value)
        # TODO: Make sure to fix programTable as well after changing the program memory
