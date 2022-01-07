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
        self.flags = [0,  # Zero
                      0,  # Sign
                      0,  # Parity
                      0,  # Carry
                      0  # Auxiliary Carry
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

    def set_cy_ca_flags(self, cy, ca):
        self.set_carry_flag(cy)
        self.set_auxiliary_carry_flag(ca)

    def binary_add(self, op1, op2, carry):
        mask = 0x01
        number, ca, cy = 0, 0, 0
        for cycle in range(8):
            value = (op1 & mask) + (op2 & mask) + (carry * mask)

            number += value & mask
            mask <<= 1
            if value & mask:
                carry = 1
            else:
                carry = 0

            if cycle == 3:
                ca = carry
            if cycle == 7:
                cy = carry

        return ca, cy

    def no_flags(self):
        pass

    def aci(self, value):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val + value + self.get_carry_flag()
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ca, cy = self.binary_add(reg_a_val, value, self.get_carry_flag())
        self.set_cy_ca_flags(cy, ca)

    def adc(self, value):
        self.aci(value)

    def add(self, value):
        reg_a = char_to_reg('a')
        reg_a_val = self.registers.get_register(reg_offset + reg_a)
        result = reg_a_val + value
        new = np.uint8(result)
        self.registers.set_register8(reg_offset + reg_a, new)

        self.evaluate_zsp_flags(True, True, True, result)
        ca, cy = self.binary_add(reg_a_val, value, 0)
        self.set_cy_ca_flags(cy, ca)

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
        current = self.registers.get_register(reg8)
        new = current + 1
        self.registers.set_register8(reg_offset + reg8, new)
        self.evaluate_flags(True, True, True, False, True)

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
        pass

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
