import numpy as np


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
        self.registerArray = Intel8080.registerArray
        self.accumulator = np.uint8(0)
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

    def set_acu(self, value):
        self.accumulator = value

    def get_acu(self):
        return self.accumulator

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

    def evaluate_flags(self, z: bool, s: bool, p: bool, cy: bool, ca: bool):
        pass

    def aci(self, data):
        register = char_to_reg('a')
        current = self.registerArray.get_register(register)
        new = current + np.uint8(data + self.get_carry_flag())
        self.registerArray.set_register(register, new)
        self.evaluate_flags(True, True, True, True, True)

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
        current = self.registerArray.get_register(reg8)
        new = current + 1
        self.registerArray.set_register(reg8, new)
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
