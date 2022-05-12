import numpy as np

reg_offset = 2


class Intel8080_Registers():
    def __init__(self):
        self.registers = [np.uint16(0),  # Program Counter
                          np.uint16(100),  # Stack Pointer 100d
                          np.uint8(0),  # B-REG 000
                          np.uint8(0),  # C-REG 001
                          np.uint8(0),  # D-REG 010
                          np.uint8(0),  # E-REG 011
                          np.uint8(0),  # H-REG 100
                          np.uint8(0),  # L-REG 101
                          np.uint8(0),  # Space for better REG allocation (110 -> Memory)
                          np.uint8(0),  # A-REG 111 / Accumulator acc
                          np.uint8(0),  # W-REG
                          np.uint8(0),  # Z-REG
                          ]
        self.address_latch = np.uint16(0)
        self.instruction_register = np.uint8(0)

    def increment_pc(self):
        self.registers[0] += 1

    def set_register8(self, register, value):
        self.registers[register] = np.uint8(value)

    def set_register8_with_offset(self, register, value):
        self.registers[register + reg_offset] = np.uint8(value)

    def set_register16(self, register, value):
        self.registers[register] = np.uint16(value)

    def set_2_8bit_reg_with_offset(self, first_reg, val_16bit):
        val_16bit = np.uint16(val_16bit)
        val_h = (val_16bit & 0xff00) >> 8
        val_l = val_16bit & 0x00ff
        self.registers[first_reg + reg_offset] = np.uint8(val_h)
        self.registers[first_reg + 1 + reg_offset] = np.uint8(val_l)

    def get_register(self, register):
        register = np.uint8(register)
        return self.registers[register]

    def get_register_with_offset(self, register):
        register = np.uint8(register)
        return self.registers[register + reg_offset]

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

    def set_instruction_reg(self, value):
        self.instruction_register = np.uint8(value)

    def get_instruction_reg(self):
        return self.instruction_register

    # Invalid Operations (For the purpose of the simulation)
    def manual_latch(self, bit, value): # Technically illegal operation
        if value == 1:
            self.address_latch = self.address_latch | (1 << bit)
        elif value == 0:
            self.address_latch = self.address_latch & (~(1 << bit))
