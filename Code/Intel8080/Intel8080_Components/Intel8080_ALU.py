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
    elif reg == 'W':
        return np.uint8(8)
    elif reg == 'Z':
        return np.uint8(9)
    else:
        return np.uint8(255)


def build_16bit_from_8bit(high, low):
    return np.uint16((high << 8) | low)


class Intel8080_ALU():
    def __init__(self, Intel8080):
        self.registers = Intel8080.registers
        self.act = np.uint8(0)  # Temporary accumulator
        self.tmp = np.uint8(0)  # Temporary register
        self.flags = [False,  # Zero
                      False,  # Sign: True means negative (value > 127)
                      False,  # Parity: True means even (value % 2 == 0)
                      False,  # Carry
                      False  # Auxiliary Carry: Overflow from bit 3 to 4
                      ]
        self.alu = np.uint8(8)  # No real register
        self.alu_cy = False

    def perform_operation(self):
        pass
        # Perform an Operation with the ALU

    def get_reg8_val(self, reg8):
        return np.uint8(self.registers.get_register(reg_offset + reg8))

    def get_alu(self):
        return np.uint8(self.alu)

    def set_alu(self, value):
        self.alu = np.uint8(value)

    def get_alu_cy(self):
        return self.alu_cy

    def set_alu_cy(self, value):
        self.alu_cy = value

    def get_act(self):
        return np.uint8(self.act)

    def set_act(self, value):
        self.act = np.uint8(value)

    def get_tmp(self):
        return np.uint8(self.tmp)

    def set_tmp(self, value):
        self.tmp = np.uint8(value)

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
        if z:
            if result == 0:
                self.set_zero_flag(True)
            else:
                self.set_zero_flag(False)

        if s:
            if result > 127:
                self.set_sign_flag(True)
            else:
                self.set_sign_flag(False)

        if p:
            if result % 2 == 0:
                self.set_parity_flag(True)
            else:
                self.set_parity_flag(False)

    def set_cy_ac_flags(self, cy, ac):
        self.set_carry_flag(bool(cy))
        self.set_auxiliary_carry_flag(bool(ac))

    # 16 Bit calculation
    def binary_add(self, op1, op2, carry: int):
        mask = 0x01
        result, ac, cy = 0, 0, 0
        for cycle in range(16):
            value = (op1 & mask) + (op2 & mask) + (carry * mask)

            result += value & mask
            mask <<= 1
            if value & mask:
                carry = 1
            else:
                carry = 0

            if cycle == 3:
                ac = carry
            if cycle == 7:
                cy = carry

        return ac, cy, result

    # 16 Bit calculation
    def binary_sub(self, op1, op2):
        two_complement = (op2 ^ 0xff) + 1
        ac, cy, result = self.binary_add(op1, two_complement, 0)
        result = np.uint8(result)
        return ac, cy, result

    def no_flags(self):
        pass

    def get_sp(self):
        return np.uint16(self.registers.get_register(1))

    def get_pc(self):
        return np.uint16(self.registers.get_register(0))

    def aci(self, val_to_add):
        if self.get_carry_flag():
            val_to_add = np.uint8(val_to_add + 1)
        self.adi(val_to_add)

    def adc(self, val_to_add):
        self.aci(val_to_add)

    def add(self, val_to_add):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val + val_to_add
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ac, cy = self.binary_add(reg_a_val, val_to_add, 0)
        self.set_cy_ac_flags(cy, ac)

    def adi(self, val_to_add):
        self.add(val_to_add)

    def ana(self, val):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val & val
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ac = ((reg_a_val & 0x8) | (val & 0x8)) >> 3
        self.set_cy_ac_flags(0, ac)

    def ani(self, value):
        self.ana(value)

    def cma(self):
        reg_a_val = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        compliment = np.uint8(reg_a_val ^ 0xff)
        self.registers.set_register8(char_to_reg("a") + reg_offset, compliment)

    def cmc(self):
        self.set_carry_flag(not self.get_carry_flag())

    def cmp(self, val):
        reg_a_val = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        result = reg_a_val - val

        # TODO schauen da anscheinend alle Flags geändert werden und nicht nur zero und carry
        self.set_zero_flag(result == 0)
        self.set_carry_flag(result < 0)

    def cpi(self, val):
        self.cmp(val)

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

    def mvi(self, reg8, val):
        val = np.uint8(val)
        self.registers.set_register8(reg_offset + reg8, val)
        self.no_flags()

    def nop(self):
        pass

    def ori(self, val):
        value_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        val = np.uint8(val | value_a)
        self.registers.set_register8_with_offset(char_to_reg("a"), val)

        self.evaluate_zsp_flags(True, True, True, val)
        self.set_cy_ac_flags(False, False)

    def ral(self):
        value_a_old = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        value_a = np.uint8(value_a_old << 1)
        if self.get_carry_flag():
            value_a = np.uint8(value_a + 1)
        self.registers.set_register8_with_offset(char_to_reg("a"), value_a)

        if (value_a_old & 0b10000000) == 128:
            self.set_carry_flag(True)
        else:
            self.set_carry_flag(False)

    def rar(self):
        value_a_old = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        value_a = np.uint8(value_a_old >> 1)
        if self.get_carry_flag():
            value_a = np.uint8(value_a + 128)
        self.registers.set_register8_with_offset(char_to_reg("a"), value_a)

        if (value_a_old & 0b00000001) == 1:
            self.set_carry_flag(True)
        else:
            self.set_carry_flag(False)

    def rlc(self):
        value_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        if (value_a & 0b10000000) == 128:
            self.set_carry_flag(True)
        else:
            self.set_carry_flag(False)

        value_a = np.uint8(value_a << 1)
        if self.get_carry_flag():
            value_a = np.uint8(value_a + 1)
        self.registers.set_register8_with_offset(char_to_reg("a"), value_a)

    def rrc(self):
        value_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        if (value_a & 0b10000000) == 128:
            self.set_carry_flag(True)
        else:
            self.set_carry_flag(False)

        value_a = np.uint8(value_a >> 1)
        if self.get_carry_flag():
            value_a = np.uint8(value_a + 1)
        self.registers.set_register8_with_offset(char_to_reg("a"), value_a)

    def sbb(self, val_to_subtract):
        self.sbi(val_to_subtract)

    def sbi(self, val_to_subtract):
        if self.get_carry_flag():
            val_to_subtract = np.uint8(val_to_subtract + 1)
        self.sui(val_to_subtract)

    def stc(self):
        self.set_carry_flag(True)

    def sub(self, val_to_subtract):
        self.sui(val_to_subtract)

    def sui(self, val_to_subtract):
        value_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        result = np.uint8(value_a - val_to_subtract)
        self.registers.set_register8_with_offset(char_to_reg("a"), result)

        ac, cy = self.binary_sub(value_a, val_to_subtract)
        self.evaluate_zsp_flags(True, True, True, result)
        self.set_cy_ac_flags(cy, ac)

    def xchg(self):
        val_d = np.uint8(self.registers.get_register_with_offset(char_to_reg("d")))
        val_e = np.uint8(self.registers.get_register_with_offset(char_to_reg("e")))
        val_l = np.uint8(self.registers.get_register_with_offset(char_to_reg("l")))
        val_h = np.uint8(self.registers.get_register_with_offset(char_to_reg("h")))
        self.registers.set_register8_with_offset(char_to_reg("d"), val_h)
        self.registers.set_register8_with_offset(char_to_reg("e"), val_l)
        self.registers.set_register8_with_offset(char_to_reg("h"), val_d)
        self.registers.set_register8_with_offset(char_to_reg("l"), val_e)

    def xri(self, val):
        value_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        result = np.uint8(val ^ value_a)
        self.registers.set_register8_with_offset(char_to_reg("a"), result)

        self.evaluate_zsp_flags(True, True, True, result)
        self.set_cy_ac_flags(False, False)
