import os
from pathlib import Path

import numpy as np

from Code.Main.AbstractProcessor import AbstractProcessor
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import Intel8080_ALU, char_to_reg, build_16bit_from_8bits
from Code.Intel8080.Intel8080_Components.Intel8080_Registers import Intel8080_Registers, reg_offset
from Code.Intel8080.Intel8080_Components.Intel8080_Peripherals import Intel8080_Peripherals
from Code.Intel8080.Intel8080_Assembler import i8080asm

# rp: b -> b,c
#     d -> d,e
#     h -> h,l
#     sp -> sp
# first register is high order, second is low order

# LXI SP,0FFFFh
asm_string = """start:
mvi a, 255d
inr a
mvi a, 20d
push psw
pop psw
"""


class Intel8080(AbstractProcessor):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent = parent_window
        self.registers = Intel8080_Registers()
        self.ALU = Intel8080_ALU(self)
        self.peripherals = Intel8080_Peripherals()
        self.program = [0] * pow(2, 16)
        self.program_length = 0
        self.interrupt = False
        self.halt = False

    def nextCycle(self):
        self.registers.increment_pc()
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        if (self.get_pc() < len(self.program)) and (self.get_memory_byte(self.get_pc()) != 0):
            instruction = self.get_memory_byte(self.get_pc())
        else:
            return

        # TODO Überträge müssen noch getestet werden
        if instruction == 0xCE:
            self.ALU.aci(self.get_one_byte_data())
        elif (instruction & 0xF8) == 0x88:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                result = self.program[self.get_h_l_address()]
            else:
                result = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.adc(result)
        elif (instruction & 0xF8) == 0x80:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                result = self.get_h_l_value()
            else:
                result = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.add(result)
        elif instruction == 0xC6:
            result = self.get_one_byte_data()
            self.ALU.adi(result)
        elif (instruction & 0xF8) == 0xA0:
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                result = self.program[self.get_h_l_address()]
            else:
                result = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.ana(result)
        elif instruction == 0xE6:
            result = self.get_one_byte_data()
            self.ALU.ani(result)
        elif instruction == 0xCD:
            self.call()
            # to skip increment of pc at calls
            return
        elif instruction == 0xDC:
            self.cc()
            return
        elif instruction == 0xFC:
            self.cm()
            return
        elif instruction == 0x2F:
            self.ALU.cma()
        elif instruction == 0x3F:
            self.ALU.cmc()
        elif (instruction & 0xF8) == 0xB8:
            if self.reg_is_mem(self.get_reg8s_from_inst(instruction)):
                result = self.program[self.get_h_l_address()]
            else:
                result = self.ALU.get_reg8_val(self.get_reg8s_from_inst(instruction))
            self.ALU.cmp(result)
        elif instruction == 0xD4:
            self.cnc()
            return
        elif instruction == 0xC4:
            self.cnz()
            return
        elif instruction == 0xF4:
            self.cp()
            return
        elif instruction == 0xEC:
            self.cpe()
            return
        elif instruction == 0xFE:
            result = self.get_one_byte_data()
            self.ALU.cpi(result)
        elif instruction == 0xE4:
            self.cpo()
            return
        elif instruction == 0xCC:
            self.cz()
            return
        elif instruction == 0x27:
            self.ALU.daa()
        elif (instruction & 0xCF) == 0x09:
            self.dad(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xC7) == 0x05:
            self.dcr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x0B:
            self.dcx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xF3:
            self.di()
        elif instruction == 0xFB:
            self.ei()
        elif instruction == 0x76:
            self.hlt()
        elif instruction == 0xDD:
            self.in_put()
        elif (instruction & 0xC7) == 0x04:
            self.inr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x03:
            self.inx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xDA:
            self.jc()
            # to skip increment of pc at jumps
            return
        elif instruction == 0xFa:
            self.jm()
            return
        elif instruction == 0xC3:
            self.jmp()
            return
        elif instruction == 0xD2:
            self.jnc()
            return
        elif instruction == 0xC2:
            self.jnz()
            return
        elif instruction == 0xF2:
            self.jp()
            return
        elif instruction == 0xEA:
            self.jpe()
            return
        elif instruction == 0xE2:
            self.jpo()
            return
        elif instruction == 0xCA:
            self.jz()
            return
        elif instruction == 0x3A:
            self.lda()
        elif instruction == 0x0A:
            self.ldax_b()
        elif instruction == 0x1A:
            self.ldax_d()
        elif instruction == 0x2A:
            self.lhld()
        elif (instruction & 0xCF) == 0x01:
            self.lxi(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xC7) == 0x06:
            result = self.get_one_byte_data()
            if self.reg_is_mem(self.get_reg8d_from_inst(instruction)):
                self.set_memory_byte(self.get_h_l_address(), result)
            else:
                self.ALU.mvi(self.get_reg8d_from_inst(instruction), result)
        elif (instruction & 0xC0) == 0x40:
            self.mov(self.get_reg8s_from_inst(instruction), self.get_reg8d_from_inst(instruction))
        elif instruction == 0x00:
            self.ALU.nop()
        elif (instruction & 0xF8) == 0xB0:
            self.ora(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xF6:
            self.ALU.ori(self.get_one_byte_data())
        elif instruction == 0xD3:
            self.out_put()
        elif instruction == 0xE9:
            self.pchl()
        elif (instruction & 0xCF) == 0xC1:
            rp = self.get_reg16_from_inst(instruction)
            if self.is_rp_meaning_sp(rp):
                self.pop_psw()
            else:
                self.pop_instr(rp)
        elif (instruction & 0xCF) == 0xC5:
            rp = self.get_reg16_from_inst(instruction)
            if self.is_rp_meaning_sp(rp):
                self.push_psw()
            else:
                self.push_instr(rp)
        elif instruction == 0x17:
            self.ALU.ral()
        elif instruction == 0x1F:
            self.ALU.rar()
        elif instruction == 0xD8:
            self.ALU.rc()
        elif instruction == 0xC9:
            self.ALU.ret()
        elif instruction == 0x07:
            self.ALU.rlc()
        elif instruction == 0xF8:
            self.ALU.rm()
        elif instruction == 0xB0:
            self.ALU.rnc()
        elif instruction == 0xC0:
            self.ALU.rnz()
        elif instruction == 0xF0:
            self.ALU.rp()
        elif instruction == 0xE8:
            self.ALU.rpe()
        elif instruction == 0x70:
            self.ALU.rpo()
        elif instruction == 0x0F:
            self.ALU.rrc()
        elif (instruction & 0xC7) == 0xC7:
            self.ALU.rst()
        elif instruction == 0xC8:
            self.ALU.rz()
        elif (instruction & 0xF8) == 0x98:
            self.ALU.sbb(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xDE:
            self.ALU.sbi()
        elif instruction == 0x22:
            self.ALU.shld()
        elif instruction == 0x32:
            self.ALU.sta()
        elif instruction == 0x02:
            self.ALU.stax_b()
        elif instruction == 0x22:
            self.ALU.stax_d()
        elif instruction == 0x37:
            self.ALU.stc()
        elif (instruction & 0xF8) == 0x90:
            self.ALU.sub(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xD6:
            self.ALU.sui()
        elif instruction == 0xEB:
            self.ALU.xchg()
        elif (instruction & 0xf8) == 0xA8:
            self.ALU.xra(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xEE:
            self.ALU.xri()
        elif instruction == 0xE3:
            self.ALU.xthl()

        self.nextCycle()
        # Concrete Implementation of nextInstruction

    def load_program(self, filepath):
        # This is supposed to replace "insert_program"-method later
        with open(filepath, 'rb') as file:
            i = 0
            while True:
                byte = file.read(1)
                if byte == b'':
                    break
                else:
                    self.program[i] = np.uint8(ord(byte))
                    i += 1
            self.program_length = i

    def insert_program(self):
        output_program = "Intel8080\\Output\\program"
        parent_path = Path(os.path.abspath(os.path.curdir)).parent

        infile = parent_path.joinpath(output_program + '.com')

        with open(infile, 'rb') as file:
            i = 0
            while True:
                byte = file.read(1)
                if byte == b'':
                    break
                else:
                    self.program[i] = np.uint8(ord(byte))
                    i += 1
            self.program_length = i

    def get_address_from_memory(self, first_byte):
        low = self.get_memory_byte(first_byte)
        high = self.get_memory_byte(first_byte + 1)
        return np.uint16((high << 8) | low)

    def get_memory_byte(self, address):
        address = np.uint16(address)
        return np.uint8(self.program[address])

    def set_memory_byte(self, address, value):
        value = np.uint8(value)
        address = np.uint16(address)
        self.program[address] = value

    def get_h_l_address(self):
        low = np.uint8(self.registers.get_register(reg_offset + char_to_reg('l')))
        high = np.uint8(self.registers.get_register(reg_offset + char_to_reg('h')))
        return np.uint16((high << 8) | low)

    def get_h_l_value(self):
        return np.uint8(self.program[self.get_h_l_address()])

    def get_pc(self):
        return np.uint16(self.registers.get_register(0))

    def add_pc(self, n):
        while n > 0:
            self.registers.increment_pc()
            n -= 1

    def set_pc(self, value16):
        self.registers.set_register16(0, np.uint16(value16))

    def set_sp(self, value16):
        self.registers.set_register16(1, np.uint16(value16))

    def get_sp(self):
        return np.uint16(self.registers.get_register(1))

    def run(self):
        i8080asm.convert_to_binary(asm_string)
        self.insert_program()

        count = 0
        while count < len(self.program):
            count += 1
            self.nextInstruction()

    def get_reg8d_from_inst(self, instruction):
        return (instruction & 0x38) >> 3

    def get_reg8s_from_inst(self, instruction):
        return instruction & 0x07

    def get_reg16_from_inst(self, instruction):
        return (instruction & 0x30) >> 4

    def reg_is_mem(self, reg8):
        if reg8 == 6:
            return True
        return False

    def is_rp_meaning_sp(self, reg8):
        if reg8 == 3:
            return True
        return False

    def get_rp_values(self, rp):
        reg_h = rp * 2
        reg_l = reg_h + 1
        reg_h_value = self.registers.get_register_with_offset(reg_h)
        reg_l_value = self.registers.get_register_with_offset(reg_l)

        return reg_h_value, reg_l_value

    def set_rp_values(self, rp, high, low):
        reg_h = rp * 2
        reg_l = reg_h + 1
        self.registers.set_register8_with_offset(reg_h, high)
        self.registers.set_register8_with_offset(reg_l, low)

    def get_one_byte_data(self):
        self.add_pc(1)
        return np.uint8(self.get_memory_byte(self.get_pc()))

    def is_interrupt_enabled(self):
        return self.interrupt

    def is_halted(self):
        return self.halt

    def push_sp(self, value, offset):
        sp = self.ALU.get_sp()
        address = np.uint16(sp - offset)
        self.set_memory_byte(address, value)

    def push(self, high, low):
        self.push_sp(high, 1)
        self.push_sp(low, 2)
        new_sp = np.uint16(self.ALU.get_sp() - 2)
        self.registers.set_register16(1, new_sp)

    def pop(self):
        sp = self.get_sp()
        val_l = self.get_memory_byte(sp)
        val_h = self.get_memory_byte(np.uint16(sp + 1))
        new_sp = np.uint16(sp + 2)
        self.set_sp(new_sp)
        return val_l, val_h

    def call(self):
        self.call_on(True)

    def call_general(self, low, high):
        self.push(high, low)

        self.set_pc(build_16bit_from_8bits(high, low))

    def call_on(self, flag: bool):
        low = self.get_one_byte_data()
        high = self.get_one_byte_data()
        if flag:
            self.call_general(low, high)
        else:
            pass

    def cc(self):
        self.call_on(self.ALU.get_carry_flag())

    def cm(self):
        self.call_on(self.ALU.get_sign_flag())

    def cnc(self):
        self.call_on(not self.ALU.get_carry_flag())

    def cnz(self):
        self.call_on(not self.ALU.get_zero_flag())

    def cp(self):
        self.call_on(not self.ALU.get_sign_flag())

    def cpe(self):
        self.call_on(self.ALU.get_parity_flag())

    def cpo(self):
        self.call_on(not self.ALU.get_parity_flag())

    def cz(self):
        self.call_on(self.ALU.get_zero_flag())

    def dad(self, rp):
        if self.is_rp_meaning_sp(rp):
            reg_val = np.uint16(self.registers.get_register(1))
        else:
            reg_h_value, reg_l_value = self.get_rp_values(rp)
            reg_val = build_16bit_from_8bits(reg_h_value, reg_l_value)

        h_val = self.registers.get_register_with_offset(char_to_reg("h"))
        l_val = self.registers.get_register_with_offset(char_to_reg("l"))
        hl_val = build_16bit_from_8bits(h_val, l_val)

        result = np.uint16(hl_val + reg_val)
        result_h = (result & 0xff00) >> 8
        result_l = result & 0x00ff
        self.registers.set_register8_with_offset(char_to_reg("h"), result_h)
        self.registers.set_register8_with_offset(char_to_reg("l"), result_l)

        if result > (pow(2, 16) - 1):
            self.ALU.set_carry_flag(True)
        else:
            self.ALU.set_carry_flag(False)

    def dcr(self, register):
        if self.reg_is_mem(register):
            value = np.uint8(self.program[self.get_h_l_address()])
            result = np.uint8(value - 1)
            self.set_memory_byte(self.get_h_l_address(), result)
        else:
            value = np.uint8(self.ALU.get_reg8_val(register))
            result = np.uint8(value - 1)
            self.registers.set_register8_with_offset(register, result)

        self.ALU.evaluate_zsp_flags(True, True, True, result)
        ac, cy = self.ALU.binary_sub(value, 1)
        self.ALU.set_auxiliary_carry_flag(ac)

    def dcx(self, rp):
        if self.is_rp_meaning_sp(rp):
            reg_val = np.uint16(self.registers.get_register(1))
            result = np.uint16(reg_val - 1)
            self.set_sp(result)
        else:
            reg_h_value, reg_l_value = self.get_rp_values(rp)
            reg_val = build_16bit_from_8bits(reg_h_value, reg_l_value)
            result = np.uint16(reg_val - 1)
            self.registers.set_2_8bit_reg_with_offset((rp * 2), result)

    def di(self):
        self.interrupt = False

    def ei(self):
        self.interrupt = True

    def hlt(self):
        self.halt = True

    def in_put(self):
        # TODO Daten müssen noch irgendwo her kommen
        data = self.get_byte_from_data_bus()
        self.registers.set_register8_with_offset(char_to_reg("a"), data)

    def inr(self, register):
        if self.reg_is_mem(register):
            value = self.get_h_l_value()
            result = np.uint8(value + 1)
            ac, cy = self.ALU.binary_add(value, 1, 0)
            self.set_memory_byte(self.get_h_l_address(), result)
        else:
            value = self.registers.get_register_with_offset(register)
            result = np.uint8(value + 1)
            ac, cy = self.ALU.binary_add(value, 1, 0)
            self.registers.set_register8_with_offset(register, result)

        self.ALU.evaluate_zsp_flags(True, True, True, result)
        self.ALU.set_auxiliary_carry_flag(ac)

    # Eine Dokumentation sagt, dass "inx e" auch möglich und würde den carry vom low byte zum high byte nicht verwenden
    # andere sagt dass es gar nicht möglich ist. Momentaner compiler kann "inx e" nicht. Instruction Code ist
    # dann 0x76 = NOP
    def inx(self, rp):
        if self.is_rp_meaning_sp(rp):
            reg_val = np.uint16(self.registers.get_register(1))
            result = np.uint16(reg_val + 1)
            self.set_sp(result)
        else:
            reg_h_value, reg_l_value = self.get_rp_values(rp)
            reg_val = build_16bit_from_8bits(reg_h_value, reg_l_value)
            result = np.uint16(reg_val + 1)
            self.registers.set_2_8bit_reg_with_offset(rp * 2, result)

    def jump_general(self, low, high):
        self.set_pc(build_16bit_from_8bits(high, low))

    def jump_on(self, flag: bool):
        low = self.get_one_byte_data()
        high = self.get_one_byte_data()
        if flag:
            self.jump_general(low, high)
        else:
            pass

    def jc(self):
        self.jump_on(self.ALU.get_carry_flag())

    def jm(self):
        self.jump_on(self.ALU.get_sign_flag())

    def jmp(self):
        self.jump_on(True)

    def jnc(self):
        self.jump_on(not self.ALU.get_carry_flag())

    def jnz(self):
        self.jump_on(not self.ALU.get_zero_flag())

    def jp(self):
        self.jump_on(not self.ALU.get_sign_flag())

    def jpe(self):
        self.jump_on(self.ALU.get_parity_flag())

    def jpo(self):
        self.jump_on(not self.ALU.get_parity_flag())

    def jz(self):
        self.jump_on(self.ALU.get_zero_flag())

    def lda(self):
        low = self.get_one_byte_data()
        high = self.get_one_byte_data()
        address = build_16bit_from_8bits(high, low)
        value = self.get_memory_byte(address)
        self.registers.set_register8_with_offset(char_to_reg("a"), value)

    def ldax(self, address_l, address_h):
        address = build_16bit_from_8bits(address_h, address_l)
        value = self.get_memory_byte(address)
        self.registers.set_register8_with_offset(char_to_reg("a"), value)

    def ldax_b(self):
        address_h = self.registers.get_register_with_offset(char_to_reg("b"))
        address_l = self.registers.get_register_with_offset(char_to_reg("c"))
        self.ldax(address_l, address_h)

    def ldax_d(self):
        address_h = self.registers.get_register_with_offset(char_to_reg("d"))
        address_l = self.registers.get_register_with_offset(char_to_reg("e"))
        self.ldax(address_l, address_h)

    def lhld(self):
        low = self.get_one_byte_data()
        high = self.get_one_byte_data()

        address_l = build_16bit_from_8bits(high, low)
        value_l = self.get_memory_byte(address_l)
        self.registers.set_register8_with_offset(char_to_reg("l"), value_l)

        address_h = np.uint16(address_l + 1)
        value_h = self.get_memory_byte(address_h)
        self.registers.set_register8_with_offset(char_to_reg("h"), value_h)

    def lxi(self, rp):
        low = self.get_one_byte_data()
        high = self.get_one_byte_data()

        if self.is_rp_meaning_sp(rp):
            value = build_16bit_from_8bits(high, low)
            self.set_sp(value)
        else:
            reg_h = rp * 2
            reg_l = reg_h + 1
            self.registers.set_register8_with_offset(reg_h, high)
            self.registers.set_register8_with_offset(reg_l, low)

    def mov(self, from_, to):
        if to == from_:
            pass

        if self.reg_is_mem(from_):
            value = self.get_h_l_value()
        else:
            value = np.uint8(self.registers.get_register_with_offset(from_))

        if self.reg_is_mem(to):
            address = self.get_h_l_address()
            self.set_memory_byte(address, value)
        else:
            self.registers.set_register8_with_offset(to, value)

    def ora(self, register):
        if self.reg_is_mem(register):
            value = self.get_h_l_value()
        else:
            value = np.uint8(self.registers.get_register_with_offset(register))

        value_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        value = np.uint8(value | value_a)
        self.registers.set_register8_with_offset(char_to_reg("a"), value)

        self.ALU.evaluate_zsp_flags(True, True, True, value)
        self.ALU.set_cy_ac_flags(False, False)

    def out_put(self):
        # TODO Daten müssen noch wohin
        data = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        self.write_byte_on_data_bus(data)

        exp = self.get_one_byte_data()
        port_address = build_16bit_from_8bits(exp, exp)
        self.write_address_on_address_bus(port_address)
        pass

    def pchl(self):
        val_h = np.uint8(self.registers.get_register_with_offset(char_to_reg("h")))
        val_l = np.uint8(self.registers.get_register_with_offset(char_to_reg("l")))
        value = build_16bit_from_8bits(val_h, val_l)
        self.set_pc(value)

    def pop_instr(self, rp):
        val_l, val_h = self.pop()
        self.set_rp_values(rp, val_h, val_l)

    def pop_psw(self):
        val_flags, val_a = self.pop()

        self.set_processor_status_word(val_flags)
        self.registers.set_register8_with_offset(char_to_reg("a"), val_a)

    def push_instr(self, rp):
        reg_h_value, reg_l_value = self.get_rp_values(rp)
        self.push(reg_h_value, reg_l_value)

    def push_psw(self):
        val_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        self.push_sp(val_a, 1)

        val_flags = self.get_processor_status_word()
        self.push_sp(val_flags, 2)

        new_sp = np.uint16(self.ALU.get_sp() - 2)
        self.registers.set_register16(1, new_sp)

    def get_processor_status_word(self):
        s = np.uint8(int(self.ALU.get_sign_flag()))
        z = np.uint8(int(self.ALU.get_zero_flag()))
        ac = np.uint8(int(self.ALU.get_auxiliary_carry_flag()))
        p = np.uint8(int(self.ALU.get_parity_flag()))
        cy = np.uint8(int(self.ALU.get_carry_flag()))

        # Byte besteht aus  7 6 5 4  3 2 1 0
        #                   s z 0 ac 0 p 1 cy
        byte = cy + 2 + p * pow(2, 2) + ac * pow(2, 4) + z * pow(2, 6) + s * pow(2, 7)
        return np.uint8(byte)

    def set_processor_status_word(self, byte):
        self.ALU.set_sign_flag((byte & pow(2, 7)) >> 7)
        self.ALU.set_zero_flag((byte & pow(2, 6)) >> 6)
        self.ALU.set_auxiliary_carry_flag((byte & pow(2, 4)) >> 4)
        self.ALU.set_parity_flag((byte & pow(2, 2)) >> 2)
        self.ALU.set_carry_flag(byte & pow(2, 0))
