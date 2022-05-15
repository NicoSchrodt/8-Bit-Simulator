import os

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.uic import loadUi

from Code.Intel8080.Intel8080_Assembler import i8080asm


def reset_ASM():
    # Current source line number.
    i8080asm.lineno = 0

    # Address of current instruction.
    i8080asm.address = 0

    # This is a 2-pass assembler, so keep track of which pass we're in.
    i8080asm.source_pass = 1

    # Assembled machine code.
    i8080asm.output = b''

    # Tokens
    i8080asm.label = ''
    i8080asm.mnemonic = ''
    i8080asm.operand1 = ''
    i8080asm.operand2 = ''
    i8080asm.comment = ''

    # Symbol table: {'label1': <address1>, 'label2': <address2>, ...}
    i8080asm.symbol_table = {}

    # Immediate operand type, 8-bit or 16-bit. An enum would be overkill and verbose.
    i8080asm.IMMEDIATE8 = 8
    i8080asm.IMMEDIATE16 = 16

    # Default output file name
    i8080asm.OUTFILE = 'program'


class ProgramEditor(QMainWindow):
    def __init__(self, parent=None):
        super(ProgramEditor, self).__init__(None)
        self.init_ui("ui\\ProgramEditor.ui")

        self.outputFile_button.pressed.connect(self.output_file)

        self.setWindowIcon(QIcon("../ui/Logo.png"))

    def init_ui(self, ui_name):
        base_path = os.path.abspath("..")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def output_file(self):
        try:
            txt = self.ProgramText.toPlainText()
            name = self.name_le.text()
            reset_ASM()
            i8080asm.convert_to_binary(txt, name)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon["Critical"])
            msg.setText("Error")
            msg.setInformativeText("Didn't work, due to error: " + i8080asm.error)
            msg.setWindowTitle("Error")
            msg.exec()

