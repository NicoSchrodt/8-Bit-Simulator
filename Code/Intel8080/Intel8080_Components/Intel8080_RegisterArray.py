import numpy as np


class Intel8080_RegisterArray():
    def __init__(self):
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
                          np.uint8(0),  # W-REG
                          np.uint8(0),  # Z-REG
                          ]
        self.address_latch = np.uint16(0)

    def increment_pc(self):
        self.registers[0] += 1

    def set_register(self, register, value):
        self.registers[register] = value

    def get_register(self, register):
        return self.registers[register]

    def fill_latch(self, register_pair):
        pair_value = 0
        if register_pair == 0:
            pair_value = int(str(bin(self.registers[2])) + str(bin(self.registers[3])))
        elif register_pair == 1:
            pair_value = int(str(bin(self.registers[4])) + str(bin(self.registers[5])))
        elif register_pair == 2:
            pair_value = int(str(bin(self.registers[6])) + str(bin(self.registers[7])))
        else:
            raise ValueError("Invalid Register Pair")
        self.address_latch = pair_value
        # If I understood it correctly, the latch can only receive data in pairs from BC, DE and HL
        # Other registers can only be read in 8-bit through the multiplexer (Except SP and PC ?)
