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
                          np.uint8(0),  # H-REG
                          np.uint8(0),  # L-REG
                          np.uint8(0),  # D-REG
                          np.uint8(0),  # E-REG
                          np.uint8(0),  # B-REG
                          np.uint8(0),  # C-REG
                          np.uint8(0),  # W-REG
                          np.uint8(0),  # Z-REG
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

        #ldax b
        if instruction == 0x0A:
            a = 0
        elif instruction == 0xFE:
            data = self.get_byte(self.get_pc() + 1)
            self.add_pc(1)
        elif instruction == 0xCA:
            address = self.get_address(self.get_pc() + 1)
            self.set_pc(address)

        if instruction == 0xce:
            self.aci()
        elif (instruction | 0xf8) == 0x88:
            self.adc(self.get_reg8s_from_inst(instruction))
        elif (instruction | 0xf8) == 0x80:
            self.add(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xc6:
            self.adi()
        elif (instruction | 0xf8) == 0xa0:
            self.ana(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xe6:
            self.ani()
        elif instruction == 0xcd:
            self.call()
        elif instruction == 0xdc:
            self.cc()
        elif instruction == 0xfc:
            self.cm()
        elif instruction == 0x2f:
            self.cma()
        elif instruction == 0x3f:
            self.cmc()
        elif (instruction | 0xf8) == 0xb8:
            self.cmp(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xd4:
            self.cnc()
        elif instruction == 0xc4:
            self.cnz()
        elif instruction == 0xf4:
            self.cp()
        elif instruction == 0xec:
            self.cpe()
        elif instruction == 0xfe:
            self.cpi()
        elif instruction == 0xe4:
            self.cpo()
        elif instruction == 0xcc:
            self.cz()
        elif instruction == 0x27:
            self.daa()
        elif (instruction | 0xcf) == 0x9:
            self.dad(self.get_reg16_from_inst(instruction))
        elif (instruction | 0xc7) == 0x05:
            self.dcr(self.get_reg8d_from_inst(instruction))




        elif (instruction | 0xc7) == 0x04:
            self.inr(self.get_reg8d_from_inst(instruction))
        # elif instruction == 0x34:
        #     inr_m()
        # elif instruction == 0x03c:
        #     inr_r_a()
        # elif instruction == 0x04:
        #     inr_r_b()
        # elif instruction == 0x0c:
        #     inr_r_c()
        # elif instruction == 0x14:
        #     inr_r_d()
        # elif instruction == 0x1c:
        #     inr_r_e()
        # elif instruction == 0x24:
        #     inr_r_h()
        # elif instruction == 0x2c:
        #     inr_r_l()
        elif (instruction | 0xcf) == 0x03:
            self.inx(self.get_reg16_from_inst(instruction))
        # elif instruction == 0x03:
        #     inx_b()
        # elif instruction == 0x13:
        #     inx_d()
        # elif instruction == 0x23:
        #     inx_h()
        elif instruction == 0x0a:
            self.ldax_b()
        elif instruction == 0x1a:
            self.ldax_d()
        elif (instruction | 0xcf) == 0x01:
            self.lxi(self.get_reg16_from_inst(instruction))
        # elif instruction == 0x01:
        #     lxi_b()
        # elif instruction == 0x11:
        #     lxi_d()
        # elif instruction == 0x21:
        #     lxi_h()
        elif (instruction | 0xc7) == 0x06:
            self.mvi(self.get_reg8d_from_inst(instruction))
        elif instruction == 0x00:
            self.nop()
        elif instruction == 0x07:
            self.rlc()
        elif instruction == 0x02:
            self.stax_b()
        elif instruction == 0x22:
            self.stax_d()

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
        return (instruction | 0x38) >> 3

    def get_reg8s_from_inst(self, instruction):
        return instruction >> 3

    def get_reg16_from_inst(self, instruction):
        return (instruction | 0x30) >> 4


    def nop(self):
        pass

    def lxi(self, reg16):
        pass

    def stax_b(self):
        pass

    def stax_d(self):
        pass

    def inx(self, reg16):
        pass

    def inr(self, reg8):
        pass

    def dcr(self, reg8):
        pass

    def mvi(self, reg8):
        pass

    def rlc(self):
        pass



    def ldax_b(self):
        pass

    def ldax_d(self):
        pass


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
        pass

    def cpo(self):
        pass

    def cz(self):
        pass

    def daa(self):
        pass

    def dad(self, reg16):
        pass
