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
    def __init__(self):
        self.registers = [np.uint8(0),  # B-REG 000
                          np.uint8(0),  # C-REG 001
                          np.uint8(0),  # D-REG 010
                          np.uint8(0),  # E-REG 011
                          np.uint8(0),  # H-REG 100
                          np.uint8(0),  # L-REG 101
                          np.uint8(0),  # Lücke für bessere REG zuweisung (110 -> Memory)
                          np.uint8(0),  # A-REG 111 (Akkumulator)
                          np.uint8(0),  # W-REG
                          np.uint8(0),  # Z-REG
                          np.uint16(0),  # Program Counter
                          np.uint16(0),  # Stack Pointer
                          ]
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

    def evaluate_flags(self, z: bool, s: bool, p: bool, cy: bool, ca: bool):
        pass

    def aci(self, data):
        self.registers[char_to_reg('a')] += np.uint8(data + self.get_carry_flag())
        self.evaluate_flags(True, True, True, True, True)
        return

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
        self.registers[reg8] += 1
        self.evaluate_flags(True, True, True, False, True)
        return

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

    def get_zero_flag(self):
        return self.flags[0]

    def get_sign_flag(self):
        return self.flags[1]

    def get_parity_flag(self):
        return self.flags[2]

    def get_carry_flag(self):
        return self.flags[3]

    def get_aux_carry(self):
        return self.flags[4]
