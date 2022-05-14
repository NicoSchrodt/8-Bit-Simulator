import os
from pathlib import Path

import numpy as np

from Code.Intel8080.CycleClasses.Childs.Instructions.Aci import Aci
from Code.Intel8080.CycleClasses.Childs.Instructions.Adc_m import Adc_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Adc_r import Adc_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Add_m import Add_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Add_r import Add_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Adi import Adi
from Code.Intel8080.CycleClasses.Childs.Instructions.Ana_m import Ana_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Ana_r import Ana_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Ani import Ani
from Code.Intel8080.CycleClasses.Childs.Instructions.Call import Call
from Code.Intel8080.CycleClasses.Childs.Instructions.Call_cond import Call_cond
from Code.Intel8080.CycleClasses.Childs.Instructions.Cma import Cma
from Code.Intel8080.CycleClasses.Childs.Instructions.Cmc import Cmc
from Code.Intel8080.CycleClasses.Childs.Instructions.Cmp_m import Cmp_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Cmp_r import Cmp_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Cpi import Cpi
from Code.Intel8080.CycleClasses.Childs.Instructions.Daa import Daa
from Code.Intel8080.CycleClasses.Childs.Instructions.Dad import Dad
from Code.Intel8080.CycleClasses.Childs.Instructions.Dcr_m import Dcr_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Dcr_r import Dcr_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Dcx import Dcx
from Code.Intel8080.CycleClasses.Childs.Instructions.Di import Di
from Code.Intel8080.CycleClasses.Childs.Instructions.Ei import Ei
from Code.Intel8080.CycleClasses.Childs.Instructions.Hlt import Hlt
from Code.Intel8080.CycleClasses.Childs.Instructions.In_inst import In_inst
from Code.Intel8080.CycleClasses.Childs.Instructions.Inr_m import Inr_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Inr_r import Inr_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Interrupt import Interrupt
from Code.Intel8080.CycleClasses.Childs.Instructions.Inx import Inx
from Code.Intel8080.CycleClasses.Childs.Instructions.Jmp import Jmp
from Code.Intel8080.CycleClasses.Childs.Instructions.Jmp_cond import Jmp_cond
from Code.Intel8080.CycleClasses.Childs.Instructions.Lda import Lda
from Code.Intel8080.CycleClasses.Childs.Instructions.Ldax import Ldax
from Code.Intel8080.CycleClasses.Childs.Instructions.Lhld import Lhld
from Code.Intel8080.CycleClasses.Childs.Instructions.Lxi import Lxi
from Code.Intel8080.CycleClasses.Childs.Instructions.Mov_m_r import Mov_m_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Mov_r_m import Mov_r_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Mov_r_r import Mov_r_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Mvi_m import Mvi_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Mvi_r import Mvi_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Nop import Nop
from Code.Intel8080.CycleClasses.Childs.Instructions.Ora_m import Ora_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Ora_r import Ora_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Ori import Ori
from Code.Intel8080.CycleClasses.Childs.Instructions.Out_inst import Out_inst
from Code.Intel8080.CycleClasses.Childs.Instructions.Pchl import Pchl
from Code.Intel8080.CycleClasses.Childs.Instructions.Pop_psw import Pop_psw
from Code.Intel8080.CycleClasses.Childs.Instructions.Pop_rp import Pop_rp
from Code.Intel8080.CycleClasses.Childs.Instructions.Push_psw import Push_psw
from Code.Intel8080.CycleClasses.Childs.Instructions.Push_rp import Push_rp
from Code.Intel8080.CycleClasses.Childs.Instructions.Ral import Ral
from Code.Intel8080.CycleClasses.Childs.Instructions.Rar import Rar
from Code.Intel8080.CycleClasses.Childs.Instructions.Ret import Ret
from Code.Intel8080.CycleClasses.Childs.Instructions.Ret_cond import Ret_cond
from Code.Intel8080.CycleClasses.Childs.Instructions.Rlc import Rlc
from Code.Intel8080.CycleClasses.Childs.Instructions.Rrc import Rrc
from Code.Intel8080.CycleClasses.Childs.Instructions.Rst import Rst
from Code.Intel8080.CycleClasses.Childs.Instructions.Sbb_m import Sbb_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Sbb_r import Sbb_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Shld import Shld
from Code.Intel8080.CycleClasses.Childs.Instructions.Sphl import Sphl
from Code.Intel8080.CycleClasses.Childs.Instructions.Sta import Sta
from Code.Intel8080.CycleClasses.Childs.Instructions.Stax import Stax
from Code.Intel8080.CycleClasses.Childs.Instructions.Stc import Stc
from Code.Intel8080.CycleClasses.Childs.Instructions.Sub_m import Sub_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Sub_r import Sub_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Sui import Sui
from Code.Intel8080.CycleClasses.Childs.Instructions.Xchg import Xchg
from Code.Intel8080.CycleClasses.Childs.Instructions.Xra_m import Xra_m
from Code.Intel8080.CycleClasses.Childs.Instructions.Xra_r import Xra_r
from Code.Intel8080.CycleClasses.Childs.Instructions.Xri import Xri
from Code.Intel8080.CycleClasses.Childs.Instructions.Xthl import Xthl
from Code.Intel8080.StateLogger import DummyLogger
from Code.Main.AbstractProcessor import AbstractProcessor
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import Intel8080_ALU, char_to_reg, build_16bit_from_8bit
from Code.Intel8080.Intel8080_Components.Intel8080_Registers import Intel8080_Registers, reg_offset
from Code.Intel8080.Intel8080_Components.Intel8080_Peripherals import Intel8080_Peripherals
from Code.Intel8080.Intel8080_Assembler import i8080asm


class Intel8080(AbstractProcessor):
    def __init__(self, parent_window=None, logger=DummyLogger()):
        super().__init__()
        self.parent = parent_window
        self.registers = Intel8080_Registers()
        self.ALU = Intel8080_ALU(self)
        self.peripherals = Intel8080_Peripherals()
        self.StateLogger = logger

        self.program = [0] * pow(2, 16)
        self.program_length = 0
        self.interrupt_enabled = True
        self.interrupted = False
        self.interrupt_instruction = 0xC7  # RST 0H = 0xC7
        self.halted = False

        self.cpu_instruction_register = np.uint8(0x00)
        self.current_instruction = Nop(self)
        self.current_instruction_state = 1
        self.current_machine_cycle = 1

        self.quittable = True
        self.instruction_counter = 0

        self.rp_mask = 0x30
        self.rp_inv_mask = self.rp_mask ^ 0xff
        self.sss_mask = 0x07
        self.sss_inv_mask = self.sss_mask ^ 0xff
        self.ddd_mask = 0x38
        self.ddd_inv_mask = self.ddd_mask ^ 0xff

        self.skip_rest_of_instruction = False
        self.c_cond_skip = False

        # rp: b -> b,c
        #     d -> d,e
        #     h -> h,l
        #     sp -> sp
        # first register is high order, second is low order

        # LXI SP,0FFFFh
        self.asm_string = """start:
        mvi h, 12d
        mvi l, 34d
        mvi b, 11d
        mvi c, 22d
        push b
        xthl
        """

    def init(self, programm):
        self.asm_string = programm
        i8080asm.convert_to_binary(self.asm_string)
        self.insert_program()

    def init_test(self, programm):
        self.asm_string = programm
        self.reset_ASM()
        i8080asm.convert_to_binary(self.asm_string, "Output\\program")
        self.insert_program("Output\\program")

    def reset_ASM(self):
        # Current source line number.
        i8080asm.lineno = 0

        # Address of current instruction.
        i8080asm.address = 0

        # This is a 2-pass assembler, so keep track of which pass we're in.
        i8080asm.source_pass = 1

        # Assembled machine code.
        i8080asm.output = b''

        # Tokens
        i8080asm.label = ''
        i8080asm.mnemonic = ''
        i8080asm.operand1 = ''
        i8080asm.operand2 = ''
        i8080asm.comment = ''

        # Symbol table: {'label1': <address1>, 'label2': <address2>, ...}
        i8080asm.symbol_table = {}

        # Immediate operand type, 8-bit or 16-bit. An enum would be overkill and verbose.
        i8080asm.IMMEDIATE8 = 8
        i8080asm.IMMEDIATE16 = 16

        # Default output file name
        i8080asm.OUTFILE = 'program'

    def next_instruction(self):
        while not self.next_machine_cycle():
            pass

        return self.current_instruction_state == 1

    def next_machine_cycle(self):
        while not self.next_state_internal():
            pass

        return self.current_instruction_state == 1

    def next_state(self):
        self.next_state_internal()

        return self.current_instruction_state == 1

    def next_state_internal(self):
        if self.current_instruction_state == 1:
            self.current_instruction = Nop(self)
            print("-------------------new Instruction-------------------")  # TODO HALT MODE
            self.StateLogger.addEntry("----new Instruction----")
            if self.interrupted:
                if self.interrupt_enabled:
                    self.current_instruction = Interrupt(self)
                    self.interrupted = False
                    self.halted = False
                    self.StateLogger.addEntry("----Interrupt acknowledged----")
                else:
                    self.StateLogger.addEntry("----Interrupt is disabled----")

        if self.halted:
            self.StateLogger.addEntry("----Halt Mode----")
            return True

        if self.current_instruction_state == 4:
            self.decode_instruction()

        if self.current_instruction.next_state():
            self.current_instruction_state += 1
            if self.current_machine_cycle == len(
                    self.current_instruction.get_machine_cycles()) or self.skip_rest_of_instruction:
                self.skip_rest_of_instruction = False
                self.current_instruction_state = 1
                self.current_machine_cycle = 1
            else:
                self.current_machine_cycle += 1
            return True
        else:
            self.current_instruction_state += 1
            return False

    def run_complete_programm(self, max_instructions=-1):
        if max_instructions == -1:
            self.quittable = False

        while not (self.quittable and not self.instruction_counter < max_instructions):
            if self.next_instruction():
                self.instruction_counter += 1

    def decode_instruction(self):
        if self.cpu_instruction_register == 0xCE:
            self.current_instruction = Aci(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0x80:
            if self.cpu_instruction_register == 0x86:
                self.current_instruction = Add_m(self)
            else:
                self.current_instruction = Add_r(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0x88:
            if self.cpu_instruction_register == 0x8E:
                self.current_instruction = Adc_m(self)
            else:
                self.current_instruction = Adc_r(self)
        elif self.cpu_instruction_register == 0xC6:
            self.current_instruction = Adi(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0xA0:
            if self.cpu_instruction_register == 0xA6:
                self.current_instruction = Ana_m(self)
            else:
                self.current_instruction = Ana_r(self)
        elif self.cpu_instruction_register == 0xE6:
            self.current_instruction = Ani(self)
        elif self.cpu_instruction_register == 0xCD:
            self.current_instruction = Call(self)
        elif (self.cpu_instruction_register & self.ddd_inv_mask) == 0xC4:
            self.current_instruction = Call_cond(self)
        elif self.cpu_instruction_register == 0x2F:
            self.current_instruction = Cma(self)
        elif self.cpu_instruction_register == 0x3F:
            self.current_instruction = Cmc(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0xB8:
            if self.cpu_instruction_register == 0xBE:
                self.current_instruction = Cmp_m(self)
            else:
                self.current_instruction = Cmp_r(self)
        elif self.cpu_instruction_register == 0xFE:
            self.current_instruction = Cpi(self)
        elif self.cpu_instruction_register == 0x27:
            self.current_instruction = Daa(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0x09:
            self.current_instruction = Dad(self)
        elif (self.cpu_instruction_register & self.ddd_inv_mask) == 0x05:
            if self.cpu_instruction_register == 0x35:
                self.current_instruction = Dcr_m(self)
            else:
                self.current_instruction = Dcr_r(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0x0B:
            self.current_instruction = Dcx(self)
        elif self.cpu_instruction_register == 0xF3:
            self.current_instruction = Di(self)
        elif self.cpu_instruction_register == 0xFB:
            self.current_instruction = Ei(self)
        elif self.cpu_instruction_register == 0xDB:
            self.current_instruction = In_inst(self)
        elif (self.cpu_instruction_register & self.ddd_inv_mask) == 0x04:
            if self.cpu_instruction_register == 0x34:
                self.current_instruction = Inr_m(self)
            else:
                self.current_instruction = Inr_r(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0x03:
            self.current_instruction = Inx(self)
        elif (self.cpu_instruction_register & self.ddd_inv_mask) == 0xC2:
            self.current_instruction = Jmp_cond(self)
        elif self.cpu_instruction_register == 0xC3:
            self.current_instruction = Jmp(self)
        elif self.cpu_instruction_register == 0x3A:
            self.current_instruction = Lda(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0x0A:
            if self.cpu_instruction_register == 0x2A:
                self.current_instruction = Lhld(self)
            else:
                self.current_instruction = Ldax(self)
        elif self.cpu_instruction_register == 0x2A:
            self.current_instruction = Lhld(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0x01:
            self.current_instruction = Lxi(self)
        elif (self.cpu_instruction_register & 0xC0) == 0x40:
            if self.get_sss() == 0b110:
                if self.get_ddd() == 0b110:
                    self.current_instruction = Hlt(self)
                else:
                    self.current_instruction = Mov_r_m(self)
            else:
                if self.get_ddd() == 0b110:
                    self.current_instruction = Mov_m_r(self)
                else:
                    self.current_instruction = Mov_r_r(self)
        elif (self.cpu_instruction_register & 0xC7) == 0x06:
            if self.get_ddd() == 0b110:
                self.current_instruction = Mvi_m(self)
            else:
                self.current_instruction = Mvi_r(self)
        elif self.cpu_instruction_register == 0x00:
            self.current_instruction = Nop(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0xB0:
            if self.cpu_instruction_register == 0xB6:
                self.current_instruction = Ora_m(self)
            else:
                self.current_instruction = Ora_r(self)
        elif self.cpu_instruction_register == 0xF6:
            self.current_instruction = Ori(self)
        elif self.cpu_instruction_register == 0xD3:
            self.current_instruction = Out_inst(self)
        elif self.cpu_instruction_register == 0xE9:
            self.current_instruction = Pchl(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0xC1:
            if self.cpu_instruction_register == 0xF1:
                self.current_instruction = Pop_psw(self)
            else:
                self.current_instruction = Pop_rp(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0xC5:
            if self.cpu_instruction_register == 0xf5:
                self.current_instruction = Push_psw(self)
            else:
                self.current_instruction = Push_rp(self)
        elif self.cpu_instruction_register == 0x17:
            self.current_instruction = Ral(self)
        elif self.cpu_instruction_register == 0x1F:
            self.current_instruction = Rar(self)
        elif self.cpu_instruction_register == 0xC9:
            self.current_instruction = Ret(self)
        elif (self.cpu_instruction_register & self.ddd_inv_mask) == 0xC0:
            self.current_instruction = Ret_cond(self)
        elif self.cpu_instruction_register == 0x07:
            self.current_instruction = Rlc(self)
        elif self.cpu_instruction_register == 0x0F:
            self.current_instruction = Rrc(self)
        elif (self.cpu_instruction_register & self.ddd_inv_mask) == 0xC7:
            self.current_instruction = Rst(self)
            self.registers.set_register8_with_offset(char_to_reg("W"), 0)
        elif self.cpu_instruction_register == 0x22:
            self.current_instruction = Shld(self)
        elif self.cpu_instruction_register == 0xF9:
            self.current_instruction = Sphl(self)
        elif self.cpu_instruction_register == 0x32:
            self.current_instruction = Sta(self)
        elif (self.cpu_instruction_register & self.rp_inv_mask) == 0x02:
            self.current_instruction = Stax(self)
        elif self.cpu_instruction_register == 0x37:
            self.current_instruction = Stc(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0x98:
            if self.cpu_instruction_register == 0x9E:
                self.current_instruction = Sbb_m(self)
            else:
                self.current_instruction = Sbb_r(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0x90:
            if self.cpu_instruction_register == 0x96:
                self.current_instruction = Sub_m(self)
            else:
                self.current_instruction = Sub_r(self)
        elif self.cpu_instruction_register == 0xD6:
            self.current_instruction = Sui(self)
        elif self.cpu_instruction_register == 0xEB:
            self.current_instruction = Xchg(self)
        elif self.cpu_instruction_register == 0xE3:
            self.current_instruction = Xthl(self)
        elif (self.cpu_instruction_register & self.sss_inv_mask) == 0xA8:
            if self.cpu_instruction_register == 0xAE:
                self.current_instruction = Xra_m(self)
            else:
                self.current_instruction = Xra_r(self)
        elif self.cpu_instruction_register == 0xEE:
            self.current_instruction = Xri(self)
        else:
            self.current_instruction = Nop(self)
            raise Exception("Decode Instruction konnte kein passenden Befehl finden")

        self.current_instruction.load_m1_t4()

    def set_cpu_instruction_register(self, value):
        self.cpu_instruction_register = np.uint8(value)

    def set_current_instruction(self, instruction):
        self.current_instruction = instruction

    def get_nnn(self):
        return self.get_ddd()

    def get_ccc(self):
        return self.get_ddd()

    def get_sss(self):
        return np.uint8(self.cpu_instruction_register & self.sss_mask)

    def get_sss_value(self):
        return np.uint8(self.registers.get_register_with_offset(self.get_sss()))

    def get_ddd(self):
        return np.uint8((self.cpu_instruction_register & self.ddd_mask) >> 3)

    def set_ddd(self, value):
        ddd = np.uint8((self.cpu_instruction_register & self.ddd_mask) >> 3)
        self.registers.set_register8_with_offset(ddd, value)

    # returns the content of the correct address:
    # when pc = 1 then returns content of program[0], first byte of program
    def get_byte_from_memory_address_at_pc(self):
        return np.uint8(self.get_memory_byte(self.get_pc() - 1))

    def get_tmp(self):
        return self.ALU.get_tmp()

    def set_tmp(self, value):
        self.ALU.set_tmp(value)

    def get_acc(self):
        return self.registers.get_register_with_offset(char_to_reg("A"))

    def set_acc(self, value):
        self.registers.set_register8_with_offset(char_to_reg("A"), value)

    def get_wz(self):
        return build_16bit_from_8bit(self.registers.get_register_with_offset(char_to_reg("W")),
                                     self.registers.get_register_with_offset(char_to_reg("Z")))

    def set_wz(self, value):
        w = value & 0xff00
        z = value & 0x00ff
        self.registers.set_register8_with_offset(char_to_reg("W"), w)
        self.registers.set_register8_with_offset(char_to_reg("Z"), z)

    # def stateTransitions(self):
    #     self.machine_cycle.t1(self)
    #     self.machine_cycle.t2(self)
    #     if not READY and HLTA:
    #         if HLTA:
    #             x=0
    #             # Rechter Block fehlt Seite 21 Intel8080
    #         else:
    #             while not READY:
    #                 self.machine_cycle.tw(self)
    #     else:
    #         if HOLD:
    #             x=0
    #             #  Set internal Hold f/f
    #         else:
    #             self.machine_cycle.t3(self)
    #             self.machine_cycle.t4(self)
    #             self.machine_cycle.t5(self)
    #         #unterer Teil fehlt

    def nextCycle(self):
        self.registers.increment_pc()
        # Concrete Implementation of nextCycle

    def nextInstruction(self):
        if self.instruction_is_completed():
            if self.interrupted:
                self.interrupted = False
                self.interrupt_enabled = False
                self.perform_interrupt_subroutine()
                self.interrupt_enabled = True

                # to skip increment of pc
                return

        if (self.get_pc() < len(self.program)) and (self.get_memory_byte(self.get_pc()) != 0):
            instruction = self.get_memory_byte(self.get_pc())
        else:
            return

        skip_pc_incr = self.identify_and_execute_instruction(instruction)

        if not skip_pc_incr:
            self.nextCycle()
        # Concrete Implementation of nextInstruction

    def instruction_is_completed(self):
        return True

    # Any device may supply an RST instruction (and indeed may supply anyone-byte 8080 instruction).
    # 9800301D_8080_8085_Assembly_Language_Programming_Manual_May81.pdf
    def perform_interrupt_subroutine(self):
        self.identify_and_execute_instruction(self.interrupt_instruction)
        return

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
            self.set_pc(0)

    def insert_program(self, output_program="Intel8080\\Output\\program"):
        parent_path = Path(os.path.abspath(os.path.curdir)).parent

        infile = parent_path.joinpath(output_program + '.com')

        with open(infile, 'rb') as file:
            i = 0  # verändert von 0
            while True:
                byte = file.read(1)
                if byte == b'':
                    break
                else:
                    self.program[i] = np.uint8(ord(byte))
                    i += 1
            self.program_length = i

    def reset_processor(self):
        self.ALU = Intel8080_ALU(self)
        self.registers = Intel8080_Registers()
        self.peripherals = Intel8080_Peripherals()

        self.interrupt_enabled = False
        self.interrupted = False
        self.interrupt_instruction = 0xC7  # RST 0H = 0xC7
        self.halted = False

        self.cpu_instruction_register = np.uint8(0x00)
        self.current_instruction = Nop(self)
        self.current_instruction_state = 1
        self.current_machine_cycle = 1

        self.quittable = True
        self.instruction_counter = 0

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

    def set_sp_l(self, value8):
        current_sp = self.get_sp()
        new_sp = (current_sp & 0xff00) | value8
        self.set_sp(new_sp)

    def set_sp_h(self, value8):
        current_sp = self.get_sp()
        new_sp = (current_sp & 0x00ff) | (value8 << 8)
        self.set_sp(new_sp)

    def get_sp(self):
        return np.uint16(self.registers.get_register(1))

    def run(self):
        i8080asm.convert_to_binary(self.asm_string)
        self.insert_program()

        count = 0
        while count < len(self.program):
            count += 1
            self.nextInstruction()

    def get_reg8d_from_inst(self, instruction):
        return np.uint8((instruction & 0x38) >> 3)

    def get_reg8s_from_inst(self, instruction):
        return np.uint8(instruction & 0x07)

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

    def rp_means_sp(self):
        if self.get_current_rp() == 3:
            return True
        return False

    def get_current_rp(self):
        return np.uint8((self.cpu_instruction_register & self.rp_mask) >> 4)

    def get_rp_address(self):
        rp = self.get_current_rp()
        high = self.registers.get_register_with_offset(2 * rp)
        low = self.registers.get_register_with_offset(2 * rp + 1)
        return build_16bit_from_8bit(high, low)

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
        return self.interrupt_enabled

    def is_halted(self):
        return self.halted

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

    def identify_and_execute_instruction(self, instruction):
        if instruction == 0xCE:
            self.ALU.aci(self.get_one_byte_data())
        elif (instruction & 0xF8) == 0x88:
            self.adc(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xF8) == 0x80:
            self.add(self.get_reg8d_from_inst(instruction))
        elif instruction == 0xC6:
            self.ALU.adi(self.get_one_byte_data())
        elif (instruction & 0xF8) == 0xA0:
            self.ana(self.get_reg8d_from_inst(instruction))
        elif instruction == 0xE6:
            self.ALU.ani(self.get_one_byte_data())
        elif instruction == 0xCD:
            self.call()
            # to skip increment of pc at calls
            return True
        elif instruction == 0xDC:
            self.cc()
            return True
        elif instruction == 0xFC:
            self.cm()
            return True
        elif instruction == 0x2F:
            self.ALU.cma()
        elif instruction == 0x3F:
            self.ALU.cmc()
        elif (instruction & 0xF8) == 0xB8:
            self.cmp(self.get_reg8d_from_inst(instruction))
        elif instruction == 0xD4:
            self.cnc()
            return True
        elif instruction == 0xC4:
            self.cnz()
            return True
        elif instruction == 0xF4:
            self.cp()
            return True
        elif instruction == 0xEC:
            self.cpe()
            return True
        elif instruction == 0xFE:
            self.ALU.cpi(self.get_one_byte_data())
        elif instruction == 0xE4:
            self.cpo()
            return True
        elif instruction == 0xCC:
            self.cz()
            return True
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
        elif instruction == 0xDB:
            self.in_put()
        elif (instruction & 0xC7) == 0x04:
            self.inr(self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xCF) == 0x03:
            self.inx(self.get_reg16_from_inst(instruction))
        elif instruction == 0xDA:
            self.jc()
            # to skip increment of pc at jumps
            return True
        elif instruction == 0xFA:
            self.jm()
            return True
        elif instruction == 0xC3:
            self.jmp()
            return True
        elif instruction == 0xD2:
            self.jnc()
            return True
        elif instruction == 0xC2:
            self.jnz()
            return True
        elif instruction == 0xF2:
            self.jp()
            return True
        elif instruction == 0xEA:
            self.jpe()
            return True
        elif instruction == 0xE2:
            self.jpo()
            return True
        elif instruction == 0xCA:
            self.jz()
            return True
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
        elif (instruction & 0xC0) == 0x40:
            self.mov(self.get_reg8s_from_inst(instruction), self.get_reg8d_from_inst(instruction))
        elif (instruction & 0xC7) == 0x06:
            self.mvi(self.get_reg8d_from_inst(instruction))
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
            self.pop_general(self.get_reg16_from_inst(instruction))
        elif (instruction & 0xCF) == 0xC5:
            self.push_general(self.get_reg16_from_inst(instruction))
        elif instruction == 0x17:
            self.ALU.ral()
        elif instruction == 0x1F:
            self.ALU.rar()
        elif instruction == 0xD8:
            self.rc()
            # to skip increment of pc at jumps
            return True
        elif instruction == 0xC9:
            self.ret()
            return True
        elif instruction == 0x07:
            self.ALU.rlc()
        elif instruction == 0xF8:
            self.rm()
            return True
        elif instruction == 0xD0:
            self.rnc()
            return True
        elif instruction == 0xC0:
            self.rnz()
            return True
        elif instruction == 0xF0:
            self.rp()
            return True
        elif instruction == 0xE8:
            self.rpe()
            return True
        elif instruction == 0x70:
            self.rpo()
            return True
        elif instruction == 0x0F:
            self.ALU.rrc()
        elif (instruction & 0xC7) == 0xC7:
            self.rst(self.get_reg8d_from_inst(instruction))
            # to skip increment of pc at jumps
            return True
        elif instruction == 0xC8:
            self.rz()
            # to skip increment of pc at jumps
            return True
        elif (instruction & 0xF8) == 0x98:
            self.sbb(self.get_reg8d_from_inst(instruction))
        elif instruction == 0xDE:
            self.ALU.sbi(self.get_one_byte_data())
        elif instruction == 0x22:
            self.shld()
        elif instruction == 0xF9:
            self.sphl()
        elif instruction == 0x32:
            self.sta()
        elif instruction == 0x02:
            self.stax_b()
        elif instruction == 0x12:
            self.stax_d()
        elif instruction == 0x37:
            self.ALU.stc()
        elif (instruction & 0xF8) == 0x90:
            self.sub(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xD6:
            self.ALU.sui(self.get_one_byte_data())
        elif instruction == 0xEB:
            self.ALU.xchg()
        elif (instruction & 0xF8) == 0xA8:
            self.xra(self.get_reg8s_from_inst(instruction))
        elif instruction == 0xEE:
            self.ALU.xri(self.get_one_byte_data())
        elif instruction == 0xE3:
            self.xthl()

        return False

    def adc(self, reg8):
        if self.reg_is_mem(reg8):
            result = self.program[self.get_h_l_address()]
        else:
            result = self.ALU.get_reg8_val(reg8)
        self.ALU.adc(result)

    def add(self, reg8):
        if self.reg_is_mem(reg8):
            result = self.get_h_l_value()
        else:
            result = self.ALU.get_reg8_val(reg8)
        self.ALU.add(result)

    def ana(self, reg8):
        if self.reg_is_mem(reg8):
            result = self.program[self.get_h_l_address()]
        else:
            result = self.ALU.get_reg8_val(reg8)
        self.ALU.ana(result)

    def call(self):
        self.call_on(True)

    def call_general(self, low, high):
        self.push(high, low)

        self.set_pc(build_16bit_from_8bit(high, low))

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

    def cmp(self, reg8):
        if self.reg_is_mem(reg8):
            result = self.program[self.get_h_l_address()]
        else:
            result = self.ALU.get_reg8_val(reg8)
        self.ALU.cmp(result)

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
            reg_val = build_16bit_from_8bit(reg_h_value, reg_l_value)

        h_val = self.registers.get_register_with_offset(char_to_reg("h"))
        l_val = self.registers.get_register_with_offset(char_to_reg("l"))
        hl_val = build_16bit_from_8bit(h_val, l_val)

        result = np.uint16(hl_val + reg_val)
        result_h = (result & 0xff00) >> 8
        result_l = result & 0x00ff
        self.registers.set_register8_with_offset(char_to_reg("h"), result_h)
        self.registers.set_register8_with_offset(char_to_reg("l"), result_l)

        if result > (pow(2, 16) - 1):
            self.ALU.set_carry_flag(True)
        else:
            self.ALU.set_carry_flag(False)

    def dcr(self, reg8):
        if self.reg_is_mem(reg8):
            value = np.uint8(self.program[self.get_h_l_address()])
            result = np.uint8(value - 1)
            self.set_memory_byte(self.get_h_l_address(), result)
        else:
            value = np.uint8(self.ALU.get_reg8_val(reg8))
            result = np.uint8(value - 1)
            self.registers.set_register8_with_offset(reg8, result)

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
            reg_val = build_16bit_from_8bit(reg_h_value, reg_l_value)
            result = np.uint16(reg_val - 1)
            self.registers.set_2_8bit_reg_with_offset((rp * 2), result)

    def di(self):
        self.interrupt_enabled = False

    def ei(self):
        self.interrupt_enabled = True

    def hlt(self):
        self.halted = True

    def in_put(self):
        data = self.get_byte_from_data_bus()
        self.registers.set_register8_with_offset(char_to_reg("a"), data)

    def inr(self, reg8):
        if self.reg_is_mem(reg8):
            value = self.get_h_l_value()
            result = np.uint8(value + 1)
            ac, cy = self.ALU.binary_add(value, 1, 0)
            self.set_memory_byte(self.get_h_l_address(), result)
        else:
            value = self.registers.get_register_with_offset(reg8)
            result = np.uint8(value + 1)
            ac, cy = self.ALU.binary_add(value, 1, 0)
            self.registers.set_register8_with_offset(reg8, result)

        self.ALU.evaluate_zsp_flags(True, True, True, result)
        self.ALU.set_auxiliary_carry_flag(ac)

    # Eine Dokumentation sagt, dass "inx e" auch möglich ist und würde den carry vom low byte zum high byte nicht
    # verwenden. Andere Doku sagt, dass es gar nicht möglich ist. Momentaner Assembler kann "inx e" nicht.
    # Instruction Code ist dann 0x76 = NOP
    def inx(self, rp):
        if self.is_rp_meaning_sp(rp):
            reg_val = np.uint16(self.registers.get_register(1))
            result = np.uint16(reg_val + 1)
            self.set_sp(result)
        else:
            reg_h_value, reg_l_value = self.get_rp_values(rp)
            reg_val = build_16bit_from_8bit(reg_h_value, reg_l_value)
            result = np.uint16(reg_val + 1)
            self.registers.set_2_8bit_reg_with_offset(rp * 2, result)

    def jump_general(self, low, high):
        self.set_pc(build_16bit_from_8bit(high, low))

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
        address_l = self.get_one_byte_data()
        address_h = self.get_one_byte_data()
        self.ldax(address_l, address_h)

    def ldax(self, address_l, address_h):
        address = build_16bit_from_8bit(address_h, address_l)
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

        address_l = build_16bit_from_8bit(high, low)
        value_l = self.get_memory_byte(address_l)
        self.registers.set_register8_with_offset(char_to_reg("l"), value_l)

        address_h = np.uint16(address_l + 1)
        value_h = self.get_memory_byte(address_h)
        self.registers.set_register8_with_offset(char_to_reg("h"), value_h)

    def lxi(self, rp):
        low = self.get_one_byte_data()
        high = self.get_one_byte_data()

        if self.is_rp_meaning_sp(rp):
            value = build_16bit_from_8bit(high, low)
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

    def mvi(self, reg8):
        data = self.get_one_byte_data()
        if self.reg_is_mem(reg8):
            self.set_memory_byte(self.get_h_l_address(), data)
        else:
            self.ALU.mvi(reg8, data)

    def ora(self, reg8):
        if self.reg_is_mem(reg8):
            value = self.get_h_l_value()
        else:
            value = np.uint8(self.registers.get_register_with_offset(reg8))

        self.ALU.ori(value)

    def out_put(self):
        data = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        self.write_byte_on_data_bus(data)

        exp = self.get_one_byte_data()
        port_address = build_16bit_from_8bit(exp, exp)
        self.write_address_on_address_bus(port_address)
        pass

    def pchl(self):
        val_h = np.uint8(self.registers.get_register_with_offset(char_to_reg("h")))
        val_l = np.uint8(self.registers.get_register_with_offset(char_to_reg("l")))
        value = build_16bit_from_8bit(val_h, val_l)
        self.set_pc(value)

    def pop_general(self, rp):
        if self.is_rp_meaning_sp(rp):
            self.pop_psw()
        else:
            self.pop_instr(rp)

    def pop_instr(self, rp):
        val_l, val_h = self.pop()
        self.set_rp_values(rp, val_h, val_l)

    def pop_psw(self):
        val_flags, val_a = self.pop()

        self.set_processor_status_word(val_flags)
        self.registers.set_register8_with_offset(char_to_reg("a"), val_a)

    def push_general(self, rp):
        if self.is_rp_meaning_sp(rp):
            self.push_psw()
        else:
            self.push_instr(rp)

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
        byte = s * pow(2, 7) + z * pow(2, 6) + ac * pow(2, 4) + p * pow(2, 2) + 2 + cy
        return np.uint8(byte)

    def set_processor_status_word(self, byte):
        self.ALU.set_sign_flag((byte & pow(2, 7)) >> 7)
        self.ALU.set_zero_flag((byte & pow(2, 6)) >> 6)
        self.ALU.set_auxiliary_carry_flag((byte & pow(2, 4)) >> 4)
        self.ALU.set_parity_flag((byte & pow(2, 2)) >> 2)
        self.ALU.set_carry_flag(byte & pow(2, 0))

    def return_general(self, low, high):
        self.set_pc(build_16bit_from_8bit(high, low))

    def return_on(self, flag: bool):
        if flag:
            low, high = self.pop()
            self.return_general(low, high)
        else:
            pass

    def rc(self):
        self.return_on(self.ALU.get_carry_flag())

    def ret(self):
        self.return_on(True)

    def rm(self):
        self.return_on(self.ALU.get_sign_flag())

    def rnc(self):
        self.return_on(not self.ALU.get_carry_flag())

    def rnz(self):
        self.return_on(not self.ALU.get_zero_flag())

    def rp(self):
        self.return_on(not self.ALU.get_sign_flag())

    def rpe(self):
        self.return_on(self.ALU.get_parity_flag())

    def rpo(self):
        self.return_on(not self.ALU.get_parity_flag())

    def rz(self):
        self.return_on(self.ALU.get_zero_flag())

    def rst(self, address_code):
        pc = self.get_pc()
        pc_high = np.uint8(pc & 0xff00)
        pc_low = np.uint8(pc & 0x00ff)
        self.push(pc_high, pc_low)
        new_address = np.uint16(8 * address_code)
        self.set_pc(new_address)

    def sbb(self, reg8):
        if self.reg_is_mem(reg8):
            result = self.get_h_l_value()
        else:
            result = self.ALU.get_reg8_val(reg8)
        self.ALU.sbb(result)

    def shld(self):
        address_low = self.get_one_byte_data()
        address_high = self.get_one_byte_data()
        address = build_16bit_from_8bit(address_high, address_low)
        self.set_memory_byte(address, self.registers.get_register_with_offset(char_to_reg("l")))
        address = np.uint16(address + 1)
        self.set_memory_byte(address, self.registers.get_register_with_offset(char_to_reg("h")))

    def sphl(self):
        val_l = np.uint8(self.registers.get_register_with_offset(char_to_reg("l")))
        val_h = np.uint8(self.registers.get_register_with_offset(char_to_reg("h")))
        self.set_sp(build_16bit_from_8bit(val_h, val_l))

    def stax(self, address):
        val_a = np.uint8(self.registers.get_register_with_offset(char_to_reg("a")))
        self.set_memory_byte(address, val_a)

    def sta(self):
        address_low = self.get_one_byte_data()
        address_high = self.get_one_byte_data()
        address = build_16bit_from_8bit(address_high, address_low)
        self.stax(address)

    def stax_b(self):
        address_high = np.uint8(self.registers.get_register_with_offset(char_to_reg("b")))
        address_low = np.uint8(self.registers.get_register_with_offset(char_to_reg("c")))
        address = build_16bit_from_8bit(address_high, address_low)
        self.stax(address)

    def stax_d(self):
        address_high = np.uint8(self.registers.get_register_with_offset(char_to_reg("d")))
        address_low = np.uint8(self.registers.get_register_with_offset(char_to_reg("e")))
        address = build_16bit_from_8bit(address_high, address_low)
        self.stax(address)

    def sub(self, reg8):
        if self.reg_is_mem(reg8):
            result = self.get_h_l_value()
        else:
            result = self.ALU.get_reg8_val(reg8)
        self.ALU.sub(result)

    def xra(self, reg8):
        if self.reg_is_mem(reg8):
            value = self.get_h_l_value()
        else:
            value = np.uint8(self.registers.get_register_with_offset(reg8))
        self.ALU.xri(value)

    def xthl(self):
        stack_l, stack_h = self.pop()
        val_h = np.uint8(self.registers.get_register_with_offset(char_to_reg("h")))
        val_l = np.uint8(self.registers.get_register_with_offset(char_to_reg("l")))
        self.push(val_h, val_l)
        self.registers.set_register8_with_offset(char_to_reg("h"), stack_h)
        self.registers.set_register8_with_offset(char_to_reg("l"), stack_l)

    def set_act(self, value):
        self.ALU.set_act(value)

    def get_act(self):
        return self.ALU.get_act()

    def set_instruction_reg(self, value):
        self.registers.set_instruction_reg(value)

    def get_instruction_reg(self):
        return self.registers.get_instruction_reg()

    def set_latch_bit(self, bit, value):
        self.registers.manual_latch(bit, value)

    def set_buffer(self, value):
        self.peripherals.set_address_buffer(value)

    def get_buffer(self):
        return self.peripherals.address_buffer

    def set_reg_array_direct(self, reg, value):
        if reg.upper() not in ['W', 'Z']:
            self.registers.set_register8_with_offset(char_to_reg(reg), value)
        elif reg.upper() == 'W':
            self.registers.set_register8(10, value)
        elif reg.upper() == "Z":
            self.registers.set_register8(11, value)

    def get_reg_array_direct(self, reg):
        if reg.upper() not in ['W', 'Z']:
            return self.registers.get_register_with_offset(char_to_reg(reg))
        elif reg.upper() == 'W':
            return self.registers.get_register(10)
        elif reg.upper() == "Z":
            return self.registers.get_register(11)
