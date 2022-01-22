import numpy as np

from Code.Intel8080.Intel8080_Components.Intel8080_Registers import reg_offset


def char_to_reg(reg: chr):
    reg = reg.upper()
    if reg == 'B':
        return np.uint8(0)
    elif reg == 'C':
        return np.uint8(1)
    elif reg == 'D':
        return np.uint8(2)
    elif reg == 'E':
        return np.uint8(3)
    elif reg == 'H':
        return np.uint8(4)
    elif reg == 'L':
        return np.uint8(5)
    elif reg == 'A':
        return np.uint8(7)
    else:
        return np.uint8(255)


class Intel8080_ALU():
    def __init__(self, Intel8080):
        self.registers = Intel8080.registers
        self.temp_accumulator = np.uint8(0)
        self.flags = [False,  # Zero
                      False,  # Sign: True means negative (value > 127)
                      False,  # Parity
                      False,  # Carry
                      False  # Auxiliary Carry
                      ]
        self.temp_register = np.uint8(0)

    def perform_operation(self):
        pass
        # Perform an Operation with the ALU

    def get_reg8_val(self, reg8):
        return np.uint8(self.registers.get_register(reg_offset + reg8))

    def set_temp_acu(self, value):
        self.temp_accumulator = value

    def get_temp_acu(self):
        return self.temp_accumulator

    def set_temp_register(self, value):
        self.temp_register = value

    def get_temp_register(self):
        return self.temp_register

    def set_zero_flag(self, state):
        self.flags[0] = state

    def get_zero_flag(self):
        return self.flags[0]

    def set_sign_flag(self, state):
        self.flags[1] = state

    def get_sign_flag(self):
        return self.flags[1]

    def set_parity_flag(self, state):
        self.flags[2] = state

    def get_parity_flag(self):
        return self.flags[2]

    def set_carry_flag(self, state):
        self.flags[3] = state

    def get_carry_flag(self):
        return self.flags[3]

    def set_auxiliary_carry_flag(self, state):
        self.flags[4] = state

    def get_auxiliary_carry_flag(self):
        return self.flags[4]

    def evaluate_zsp_flags(self, z: bool, s: bool, p: bool, result):
        if z and result == 0:
            self.set_zero_flag(True)
        else:
            self.set_zero_flag(False)

        if s and result > 127:
            self.set_sign_flag(True)
        else:
            self.set_sign_flag(False)

        if p and result % 2 == 0:
            self.set_parity_flag(True)
        else:
            self.set_parity_flag(False)

    def set_cy_ac_flags(self, cy, ac):
        self.set_carry_flag(bool(cy))
        self.set_auxiliary_carry_flag(bool(ac))

    # 8 Bit calculation
    def binary_add(self, op1, op2, carry: int):
        mask = 0x01
        number, ac, cy = 0, 0, 0
        for cycle in range(8):
            value = (op1 & mask) + (op2 & mask) + (carry * mask)

            number += value & mask
            mask <<= 1
            if value & mask:
                carry = 1
            else:
                carry = 0

            if cycle == 3:
                ac = carry
            if cycle == 7:
                cy = carry

        return ac, cy

    # 8 Bit calculation
    def binary_sub(self, op1, op2):
        two_complement = (op2 ^ 0xff) + 1
        return self.binary_add(op1, two_complement, 0)

    def no_flags(self):
        pass

    def get_sp(self):
        return np.uint16(self.registers.get_register(1))

    def aci(self, value):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val + value + self.get_carry_flag()
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ac, cy = self.binary_add(reg_a_val, value, self.get_carry_flag())
        self.set_cy_ac_flags(cy, ac)

    def adc(self, value):
        self.aci(value)

    def add(self, value):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val + value
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ac, cy = self.binary_add(reg_a_val, value, 0)
        self.set_cy_ac_flags(cy, ac)

    def adi(self, value):
        self.add(value)

    def ana(self, value):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val & value
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ac = ((reg_a_val & 0x8) | (value & 0x8)) >> 3
        self.set_cy_ac_flags(0, ac)

    def ani(self, value):
        self.ana(value)

    def cma(self):
        reg_a_val = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        compliment = np.uint8(reg_a_val ^ 0xff)
        self.registers.set_register8(char_to_reg("a") + reg_offset, compliment)

    def cmc(self):
        self.set_carry_flag(not self.get_carry_flag())

    def cmp(self, value):
        reg_a_val = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))

        result = reg_a_val - value

        # TODO schauen da anscheinend alle Flags geändert werden und nicht nur zero und carry
        self.set_zero_flag(result == 0)
        self.set_carry_flag(result < 0)

    def cpi(self, value):
        self.cmp(value)

    def daa(self):
        reg_a_val = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        result = reg_a_val
        ac = self.get_auxiliary_carry_flag()
        cy = self.get_carry_flag()

        l_val = reg_a_val & 0x0f
        h_val = reg_a_val & 0xf0
        if l_val > 9 or self.get_auxiliary_carry_flag():
            ac, wrong_cy = self.binary_add(reg_a_val, 6, 0)
            self.registers.set_register8_with_offset(char_to_reg("a"), reg_a_val + 6)
        reg_a_val = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        if h_val > 9 or self.get_carry_flag():
            wrong_ac, cy = self.binary_add(reg_a_val, 6 << 4, 0)
            result = np.uint8(reg_a_val + (6 << 4))
            self.registers.set_register8_with_offset(char_to_reg("a"), result)

        self.evaluate_zsp_flags(True, True, True, result)
        self.set_cy_ac_flags(cy, ac)

    def lhld(self):
        pass

    def lxi(self, reg16):
        pass

    def mvi(self, reg8, value):
        value = np.uint8(value)
        self.registers.set_register8(reg_offset + reg8, value)
        self.no_flags()

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
