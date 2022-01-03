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
        self.programm = np.zeros(1024, dtype=np.uint8)
        self.insert_program()
        count = 0
        while count < len(self.programm):
            count += 1
            self.nextInstruction()

    def nextCycle(self):
        self.registers[0] += 1
        pass
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        instruction = self.get_byte(self.registers[0])

        #ldax b
        if instruction == 0x0A:
            a = 0
        elif instruction == 0xFE:
            data = self.get_byte(self.get_pc() + 1)
            self.add_pc(1)
        elif instruction == 0xCA:
            address = self.get_address(self.get_pc() + 1)
            self.set_pc(address)

        self.nextCycle()
        pass
        # Concrete Implementation of nextInstruction

    def insert_program(self):
        output_program = "Intel8080\\Output\\program"
        parent_path = Path(os.path.abspath(os.path.curdir)).parent

        infile = parent_path.joinpath(output_program + '.com')

        with open(infile, 'rb') as file:
            byte = file.read()
            self.programm = np.frombuffer(byte, dtype=np.uint8)
            print(self.programm)
            file.close()
        pass

    def get_address(self, first_byte):
        low = self.get_byte(first_byte)
        high = self.get_byte(first_byte + 1)
        return np.uint16((high << 8) | low)

    def get_byte(self, index):
        print(self.programm[index])
        return self.programm[index]

    def get_pc(self):
        return self.registers[0]

    def add_pc(self, n):
        while n > 0:
            self.registers[0] += 1
            n -= 1

    def set_pc(self, address):
        self.registers[0] = np.uint16(address)
