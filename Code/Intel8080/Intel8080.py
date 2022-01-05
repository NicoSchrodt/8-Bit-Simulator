import os
from pathlib import Path

import numpy as np

from Code.Main.AbstractProcessor import AbstractProcessor
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import Intel8080_ALU


class Intel8080(AbstractProcessor):
    def __init__(self):
        super().__init__()
        self.registers = [np.uint16(0),  # Program Counter
                          np.uint16(0),  # Stack Pointer
                          np.uint8(0),  # B-REG 000
                          np.uint8(0),  # C-REG 001
                          np.uint8(0),  # D-REG 010
                          np.uint8(0),  # E-REG 011
                          np.uint8(0),  # H-REG 100
                          np.uint8(0),  # L-REG 101
                          np.uint8(0),  # Lücke für bessere REG zuweisung (110 -> Memory)
                          np.uint8(0),  # A-REG 111
                          np.uint8(0),  # H-REG
                          np.uint8(0),  # L-REG
                          ]
        self.address_latch = np.uint16(0)
        self.ALU = Intel8080_ALU()
        self.program = np.zeros(1024, dtype=np.uint8)
        self.insert_program()

    def nextCycle(self):
        self.registers[0] += 1
        pass
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        if self.get_pc() < len(self.program):
            instruction = self.get_byte(self.registers[0])
        else:
            return

        if instruction == 0xCE:
            self.aci()
        elif (instruction & 0xF8) == 0x88:
            self.adc(self.get_reg8s_from_inst(instruction))
        elif (instruction & 0xF8) == 0x80:
            self.add(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xC6:
            self.adi()
        elif (instruction & 0xF8) == 0xA0:
            self.ana(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xE6:
            self.ani()
        elif instruction == 0xCD:
            self.call()
        elif instruction == 0xDC:
            self.cc()
        elif instruction == 0xFC:
            self.cm()
        elif instruction == 0x2F:
            self.cma()
        elif instruction == 0x3F:
            self.cmc()
        elif (instruction & 0xF8) == 0xB8:
            self.cmp(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xD4:
            self.cnc()
        elif instruction == 0xC4:
            self.cnz()
        elif instruction == 0xF4:
            self.cp()
        elif instruction == 0xEC:
            self.cpe()
        elif instruction == 0xFE:
            self.cpi()
        elif instruction == 0xE4:
            self.cpo()
        elif instruction == 0xCC:
            self.cz()
        elif instruction == 0x27:
            self.daa()
        elif (instruction & 0xCF) == 0x09:
            self.dad(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xC7) == 0x05:
            self.dcr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x0B:
            self.dcx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xF3:
            self.di()
        elif instruction == 0xFB:
            self.ei()
        elif instruction == 0x76:
            self.hlt()
        elif instruction == 0xDD:
            self.in_put()
        elif (instruction & 0xC7) == 0x04:
            self.inr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x03:
            self.inx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xDA:
            self.jc()
        elif instruction == 0xFa:
            self.jm()
        elif instruction == 0xC3:
            self.jmp()
        elif instruction == 0xD2:
            self.jnc()
        elif instruction == 0xC2:
            self.jnz()
        elif instruction == 0xF2:
            self.jp()
        elif instruction == 0xEA:
            self.jpe()
        elif instruction == 0xE2:
            self.jpo()
        elif instruction == 0xCA:
            self.jz()
        elif instruction == 0x3A:
            self.lda()
        elif instruction == 0x0A:
            self.ldax_b()
        elif instruction == 0x1A:
            self.ldax_d()
        elif instruction == 0x2A:
            self.lhld()
        elif (instruction & 0xCF) == 0x01:
            self.lxi(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xC7) == 0x06:
            self.mvi(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xC0) == 0x40:
            self.mov(self.get_reg8s_from_inst(instruction), self.get_reg8d_from_inst(instruction))
        elif instruction == 0x00:
            self.nop()
        elif (instruction & 0xF8) == 0xB0:
            self.ora(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xF6:
            self.ori()
        elif instruction == 0xD3:
            self.out_put()
        elif instruction == 0xE9:
            self.pchl()
        elif (instruction & 0xCF) == 0xC1:
            self.pop(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xCF) == 0xC5:
            self.push(self.get_reg16_from_inst(instruction))
        elif instruction == 0x17:
            self.ral()
        elif instruction == 0x1F:
            self.rar()
        elif instruction == 0xD8:
            self.rc()
        elif instruction == 0xC9:
            self.ret()
        elif instruction == 0x07:
            self.rlc()
        elif instruction == 0xF8:
            self.rm()
        elif instruction == 0xB0:
            self.rnc()
        elif instruction == 0xC0:
            self.rnz()
        elif instruction == 0xF0:
            self.rp()
        elif instruction == 0xE8:
            self.rpe()
        elif instruction == 0x70:
            self.rpo()
        elif instruction == 0x0F:
            self.rrc()
        elif (instruction & 0xC7) == 0xC7:
            self.rst()
        elif instruction == 0xC8:
            self.rz()
        elif (instruction & 0xF8) == 0x98:
            self.sbb(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xDE:
            self.sbi()
        elif instruction == 0x22:
            self.shld()
        elif instruction == 0x32:
            self.sta()
        elif instruction == 0x02:
            self.stax_b()
        elif instruction == 0x22:
            self.stax_d()
        elif instruction == 0x37:
            self.stc()
        elif (instruction & 0xF8) == 0x90:
            self.sub(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xD6:
            self.sui()
        elif instruction == 0xEB:
            self.xchg()
        elif (instruction & 0xf8) == 0xA8:
            self.xra(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xEE:
            self.xri()
        elif instruction == 0xE3:
            self.xthl()

        self.nextCycle()
        pass
        # Concrete Implementation of nextInstruction

    def insert_program(self):
        output_program = "Intel8080\\Output\\program"
        parent_path = Path(os.path.abspath(os.path.curdir)).parent

        infile = parent_path.joinpath(output_program + '.com')

        with open(infile, 'rb') as file:
            byte = file.read()
            self.program = np.frombuffer(byte, dtype=np.uint8)
            print(self.program)
            file.close()
        pass

    def get_address(self, first_byte):
        low = self.get_byte(first_byte)
        high = self.get_byte(first_byte + 1)
        return np.uint16((high << 8) | low)

    def get_byte(self, index):
        print(self.program[index])
        return self.program[index]

    def get_pc(self):
        return self.registers[0]

    def add_pc(self, n):
        while n > 0:
            self.registers[0] += 1
            n -= 1

    def set_pc(self, address):
        self.registers[0] = np.uint16(address)

    def run(self):
        count = 0
        while count < len(self.program):
            count += 1
            self.nextInstruction()

    def get_reg8d_from_inst(self, instruction):
        return (instruction & 0x38) >> 3

    def get_reg8s_from_inst(self, instruction):
        return instruction >> 3

    def get_reg16_from_inst(self, instruction):
        return (instruction & 0x30) >> 4

    def aci(self):
        pass

    def adc(self, reg8):
        pass

    def add(self, reg8):
        pass

    def adi(self):
        pass

    def ana(self, reg8):
        pass

    def ani(self):
        pass

    def call(self):
        pass

    def cc(self):
        pass

    def cm(self):
        pass

    def cma(self):
        pass

    def cmc(self):
        pass

    def cmp(self, reg8):
        pass

    def cnc(self):
        pass

    def cnz(self):
        pass

    def cp(self):
        pass

    def cpe(self):
        pass

    def cpi(self):
        data = self.get_byte(self.get_pc() + 1)
        self.add_pc(1)
        pass

    def cpo(self):
        pass

    def cz(self):
        pass

    def daa(self):
        pass

    def dad(self, reg16):
        pass

    def dcr(self, reg8):
        pass

    def dcx(self, reg16):
        pass

    def di(self):
        pass

    def ei(self):
        pass

    def hlt(self):
        pass

    def in_put(self):
        pass

    def inr(self, reg8):
        if reg8 == 6:   # memory
            pass
        else:
            self.registers[2 + reg8] += 1
        pass

    def inx(self, reg16):
        pass

    def jc(self):
        pass

    def jm(self):
        pass

    def jmp(self):
        pass

    def jnc(self):
        pass

    def jnz(self):
        pass

    def jp(self):
        pass

    def jpe(self):
        pass

    def jpo(self):
        pass

    def jz(self):
        address = self.get_address(self.get_pc() + 1)
        self.set_pc(address)

    def lda(self):
        pass

    def ldax_b(self):
        pass

    def ldax_d(self):
        pass

    def lhld(self):
        pass

    def lxi(self, reg16):
        pass

    def mvi(self, reg8):
        pass

    def mov(self, from_reg, to_reg):
        pass

    def nop(self):
        pass

    def ora(self, reg8):
        pass

    def ori(self):
        pass

    def out_put(self):
        pass

    def pchl(self):
        pass

    def pop(self, reg16):
        pass

    def push(self, reg16):
        pass

    def ral(self):
        pass

    def rar(self):
        pass

    def rc(self):
        pass

    def ret(self):
        pass

    def rlc(self):
        pass

    def rm(self):
        pass

    def rnc(self):
        pass

    def rnz(self):
        pass

    def rp(self):
        pass

    def rpe(self):
        pass

    def rpo(self):
        pass

    def rrc(self):
        pass

    def rst(self):
        pass

    def rz(self):
        pass

    def sbb(self, reg8):
        pass

    def sbi(self):
        pass

    def shld(self):
        pass

    def sta(self):
        pass

    def stax_b(self):
        pass

    def stax_d(self):
        pass

    def stc(self):
        pass

    def sub(self, reg8):
        pass

    def sui(self):
        pass

    def xchg(self):
        pass

    def xra(self, reg8):
        pass

    def xri(self):
        pass

    def xthl(self):
        pass
