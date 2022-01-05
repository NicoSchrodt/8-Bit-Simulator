import os
from pathlib import Path

import numpy as np

from Code.Main.AbstractProcessor import AbstractProcessor
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import Intel8080_ALU, char_to_reg
from Code.Intel8080.Intel8080_Components.Intel8080_Registers import Intel8080_Registers
from Code.Intel8080.Intel8080_Assembler import i8080asm

asm_string = """Loop:
  ldax b
  cpi 0
  jz Done
  add d
  mov d, a
  inr c
  jmp Loop

Done:
  hlt

myArray:
  db 10h, 20h, 30h, 10h, 20h, 0"""


class Intel8080(AbstractProcessor):
    def __init__(self):
        super().__init__()
        self.registers = Intel8080_Registers()
        self.ALU = Intel8080_ALU(self)
        self.program = np.zeros(1024, dtype=np.uint8)
        self.insert_program()

    def nextCycle(self):
        self.registers.increment_pc()
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        if self.get_pc() < len(self.program):
            instruction = self.get_byte(self.get_pc())
        else:
            return

        if instruction == 0xCE:
            self.ALU.aci(self.get_one_byte_data())
        elif (instruction & 0xF8) == 0x88:
            self.ALU.adc(self.get_reg8s_from_inst(instruction))
        elif (instruction & 0xF8) == 0x80:
            self.ALU.add(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xC6:
            self.ALU.adi()
        elif (instruction & 0xF8) == 0xA0:
            self.ALU.ana(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xE6:
            self.ALU.ani()
        elif instruction == 0xCD:
            self.ALU.call()
        elif instruction == 0xDC:
            self.ALU.cc()
        elif instruction == 0xFC:
            self.ALU.cm()
        elif instruction == 0x2F:
            self.ALU.cma()
        elif instruction == 0x3F:
            self.ALU.cmc()
        elif (instruction & 0xF8) == 0xB8:
            self.ALU.cmp(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xD4:
            self.ALU.cnc()
        elif instruction == 0xC4:
            self.ALU.cnz()
        elif instruction == 0xF4:
            self.ALU.cp()
        elif instruction == 0xEC:
            self.ALU.cpe()
        elif instruction == 0xFE:
            self.ALU.cpi()
        elif instruction == 0xE4:
            self.ALU.cpo()
        elif instruction == 0xCC:
            self.ALU.cz()
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
                self.program[self.get_h_l_address()] = np.uint8(self.program[self.get_h_l_address()] + 1)
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
            self.ALU.mvi(self.get_reg8d_from_inst(instruction))
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
        return np.uint8(self.program[np.uint8(index)])

    def get_h_l_address(self):
        return np.uint16((self.registers.get_register(char_to_reg('h') << 8)) |
                         self.registers.get_register(char_to_reg('l')))

    def get_pc(self):
        return self.registers.get_register(0)

    def add_pc(self, n):
        while n > 0:
            self.registers.increment_pc()
            n -= 1

    def set_pc(self, address):
        self.registers.set_register(0, np.uint16(address))

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
        return instruction >> 3

    def get_reg16_from_inst(self, instruction):
        return (instruction & 0x30) >> 4

    def reg_is_mem(self, reg8):
        if reg8 == 6:
            return True
        return False

    def get_one_byte_data(self):
        return np.uint8(self.get_byte(self.get_pc() + 1))
