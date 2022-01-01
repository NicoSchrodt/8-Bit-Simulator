import numpy as np

from ..AbstractProcessor import AbstractProcessor
from Intel8080_Components.Intel8080_ALU import Intel8080_ALU


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

    def nextCycle(self):
        pass
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        pass
        # Concrete Implementation of nextInstruction
