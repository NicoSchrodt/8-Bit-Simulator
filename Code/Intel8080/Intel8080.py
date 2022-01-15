import os
from pathlib import Path

import numpy as np

from Code.Main.AbstractProcessor import AbstractProcessor
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import Intel8080_ALU, char_to_reg
from Code.Intel8080.Intel8080_Components.Intel8080_Registers import Intel8080_Registers, reg_offset
from Code.Intel8080.Intel8080_Assembler import i8080asm


asm_string = """mvi a, 1bh
cpi 05h
"""


class Intel8080(AbstractProcessor):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent = parent_window
        self.registers = Intel8080_Registers()
        self.ALU = Intel8080_ALU(self)
        self.program = [0] * pow(2, 16)

    def nextCycle(self):
        self.registers.increment_pc()
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        if self.get_pc() < len(self.program):
            instruction = self.get_memory_byte(self.get_pc())
        else:
            return

        if instruction == 0xCE:
            self.ALU.aci(self.get_one_byte_data())
        elif (instruction & 0xF8) == 0x88:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                value = self.program[self.get_h_l_address()]
            else:
                value = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.adc(value)
        elif (instruction & 0xF8) == 0x80:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                value = self.get_h_l_value()
            else:
                value = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.add(value)
        elif instruction == 0xC6:
            value = self.get_one_byte_data()
            self.ALU.adi(value)
        elif (instruction & 0xF8) == 0xA0:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                value = self.program[self.get_h_l_address()]
            else:
                value = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.ana(value)
        elif instruction == 0xE6:
            value = self.get_one_byte_data()
            self.ALU.ani(value)
        elif instruction == 0xCD:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.call(low, high)
        elif instruction == 0xDC:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cc(low, high)
        elif instruction == 0xFC:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cm(low, high)
        elif instruction == 0x2F:
            self.ALU.cma()
        elif instruction == 0x3F:
            self.ALU.cmc()
        elif (instruction & 0xF8) == 0xB8:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                value = self.program[self.get_h_l_address()]
            else:
                value = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.cmp(value)
        elif instruction == 0xD4:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cnc(low, high)
        elif instruction == 0xC4:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cnz(low, high)
        elif instruction == 0xF4:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cp(low, high)
        elif instruction == 0xEC:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cpe(low, high)
        elif instruction == 0xFE:
            value = self.get_one_byte_data()
            self.ALU.cpi(value)
        elif instruction == 0xE4:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cpo(low, high)
        elif instruction == 0xCC:
            low = self.get_one_byte_data()
            high = self.get_one_byte_data()
            self.cz(low, high)
        elif instruction == 0x27:
            self.ALU.daa()
        elif (instruction & 0xCF) == 0x09:
            self.ALU.dad(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xC7) == 0x05:
            self.ALU.dcr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x0B:
            self.ALU.dcx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xF3:
            self.ALU.di()
        elif instruction == 0xFB:
            self.ALU.ei()
        elif instruction == 0x76:
            self.ALU.hlt()
        elif instruction == 0xDD:
            self.ALU.in_put()
        elif (instruction & 0xC7) == 0x04:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                self.set_memory_byte(self.get_h_l_address(), self.get_h_l_value() + 1)
            else:
                self.ALU.inr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x03:
            self.ALU.inx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xDA:
            self.ALU.jc()
        elif instruction == 0xFa:
            self.ALU.jm()
        elif instruction == 0xC3:
            self.ALU.jmp()
        elif instruction == 0xD2:
            self.ALU.jnc()
        elif instruction == 0xC2:
            self.ALU.jnz()
        elif instruction == 0xF2:
            self.ALU.jp()
        elif instruction == 0xEA:
            self.ALU.jpe()
        elif instruction == 0xE2:
            self.ALU.jpo()
        elif instruction == 0xCA:
            self.ALU.jz()
        elif instruction == 0x3A:
            self.ALU.lda()
        elif instruction == 0x0A:
            self.ALU.ldax_b()
        elif instruction == 0x1A:
            self.ALU.ldax_d()
        elif instruction == 0x2A:
            self.ALU.lhld()
        elif (instruction & 0xCF) == 0x01:
            self.ALU.lxi(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xC7) == 0x06:
            value = self.get_one_byte_data()
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                self.set_memory_byte(self.get_h_l_address(), value)
            else:
                self.ALU.mvi(self.get_reg8d_from_inst(instruction), value)
        elif (instruction & 0xC0) == 0x40:
            self.ALU.mov(self.get_reg8s_from_inst(instruction), self.get_reg8d_from_inst(instruction))
        elif instruction == 0x00:
            self.ALU.nop()
        elif (instruction & 0xF8) == 0xB0:
            self.ALU.ora(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xF6:
            self.ALU.ori()
        elif instruction == 0xD3:
            self.ALU.out_put()
        elif instruction == 0xE9:
            self.ALU.pchl()
        elif (instruction & 0xCF) == 0xC1:
            self.ALU.pop(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xCF) == 0xC5:
            self.ALU.push(self.get_reg16_from_inst(instruction))
        elif instruction == 0x17:
            self.ALU.ral()
        elif instruction == 0x1F:
            self.ALU.rar()
        elif instruction == 0xD8:
            self.ALU.rc()
        elif instruction == 0xC9:
            self.ALU.ret()
        elif instruction == 0x07:
            self.ALU.rlc()
        elif instruction == 0xF8:
            self.ALU.rm()
        elif instruction == 0xB0:
            self.ALU.rnc()
        elif instruction == 0xC0:
            self.ALU.rnz()
        elif instruction == 0xF0:
            self.ALU.rp()
        elif instruction == 0xE8:
            self.ALU.rpe()
        elif instruction == 0x70:
            self.ALU.rpo()
        elif instruction == 0x0F:
            self.ALU.rrc()
        elif (instruction & 0xC7) == 0xC7:
            self.ALU.rst()
        elif instruction == 0xC8:
            self.ALU.rz()
        elif (instruction & 0xF8) == 0x98:
            self.ALU.sbb(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xDE:
            self.ALU.sbi()
        elif instruction == 0x22:
            self.ALU.shld()
        elif instruction == 0x32:
            self.ALU.sta()
        elif instruction == 0x02:
            self.ALU.stax_b()
        elif instruction == 0x22:
            self.ALU.stax_d()
        elif instruction == 0x37:
            self.ALU.stc()
        elif (instruction & 0xF8) == 0x90:
            self.ALU.sub(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xD6:
            self.ALU.sui()
        elif instruction == 0xEB:
            self.ALU.xchg()
        elif (instruction & 0xf8) == 0xA8:
            self.ALU.xra(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xEE:
            self.ALU.xri()
        elif instruction == 0xE3:
            self.ALU.xthl()

        self.nextCycle()
        # Concrete Implementation of nextInstruction

    def load_program(self, filepath):
        with open(filepath, 'rb') as file:
            i = 0
            while True:
                byte = file.read(1)
                if byte == b'':
                    break
                else:
                    self.program[i] = np.uint8(ord(byte))
                    i += 1

    def insert_program(self):
        output_program = "Intel8080\\Output\\program"
        parent_path = Path(os.path.abspath(os.path.curdir)).parent

        infile = parent_path.joinpath(output_program + '.com')

        with open(infile, 'rb') as file:
            i = 0
            while True:
                byte = file.read(1)
                if byte == b'':
                    break
                else:
                    self.program[i] = np.uint8(ord(byte))
                    i += 1

    def get_address_from_memory(self, first_byte):
        low = self.get_memory_byte(first_byte)
        high = self.get_memory_byte(first_byte + 1)
        return np.uint16((high << 8) | low)

    def get_memory_byte(self, address):
        address = np.uint16(address)
        return np.uint8(self.program[address])

    def set_memory_byte(self, address, value):
        value = np.uint8(value)
        address = np.uint16(address)
        self.program[address] = value

    def get_h_l_address(self):
        low = np.uint8(self.registers.get_register(reg_offset + char_to_reg('l')))
        high = np.uint8(self.registers.get_register(reg_offset + char_to_reg('h')))
        return np.uint16((high << 8) | low)

    def get_h_l_value(self):
        return np.uint8(self.program[self.get_h_l_address()])

    def get_pc(self):
        return self.registers.get_register(0)

    def add_pc(self, n):
        while n > 0:
            self.registers.increment_pc()
            n -= 1

    def set_pc(self, address):
        self.registers.set_register16(0, np.uint16(address))

    def run(self):
        i8080asm.convert_to_binary(asm_string)
        self.insert_program()

        count = 0
        while count < len(self.program):
            count += 1
            self.nextInstruction()

    def get_reg8d_from_inst(self, instruction):
        return (instruction & 0x38) >> 3

    def get_reg8s_from_inst(self, instruction):
        return instruction & 0x07

    def get_reg16_from_inst(self, instruction):
        return (instruction & 0x30) >> 4

    def reg_is_mem(self, reg8):
        if reg8 == 6:
            return True
        return False

    def get_one_byte_data(self):
        self.add_pc(1)
        return np.uint8(self.get_memory_byte(self.get_pc()))

    def build_address(self, high, low):
        return np.uint16((high << 8) | low)

    def call(self, low, high):
        self.push_sp(high, 1)
        self.push_sp(low, 2)
        new_sp = np.uint16(self.ALU.get_sp() - 2)
        self.registers.set_register16(1, new_sp)

        self.set_pc(self.build_address(high, low))

    def push_sp(self, value, offset):
        sp = self.ALU.get_sp()
        address = np.uint16(sp - offset)
        self.set_memory_byte(address, value)

    def call_on_(self, low, high):
        pc = np.uint16(self.registers.get_register(0))
        pc_high = pc & 0xff00
        pc_low = pc & 0x00ff
        self.push_sp(pc_high, 1)
        self.push_sp(pc_low, 2)

        self.set_pc(self.build_address(high, low))

    def cc(self, low, high):
        if self.ALU.get_carry_flag():
            self.call_on_(low, high)
        else:
            pass

    def cm(self, low, high):
        if self.ALU.get_sign_flag():
            self.call_on_(low, high)
        else:
            pass

    def cnc(self, low, high):
        if not self.ALU.get_carry_flag():
            self.call_on_(low, high)
        else:
            pass

    def cnz(self, low, high):
        if not self.ALU.get_zero_flag():
            self.call_on_(low, high)
        else:
            pass

    def cp(self, low, high):
        if not self.ALU.get_sign_flag():
            self.call_on_(low, high)
        else:
            pass

    def cpe(self, low, high):
        if self.ALU.get_parity_flag():
            self.call_on_(low, high)
        else:
            pass

    def cpo(self, low, high):
        if not self.ALU.get_parity_flag():
            self.call_on_(low, high)
        else:
            pass

    def cz(self, low, high):
        if self.ALU.get_zero_flag():
            self.call_on_(low, high)
        else:
            pass
