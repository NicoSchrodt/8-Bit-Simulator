from unittest import TestCase

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.Intel8080_Assembler import i8080asm
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class TestIntel8080(TestCase):

    def test_framework(self):
        self.assertTrue(True)

    def test_Mov_r_r(self):
        with Intel8080() as intel, i8080asm as asm:
            intel.init("mov c, b")

            intel.registers.set_register8_with_offset(char_to_reg("B"), 2)  # from
            intel.registers.set_register8_with_offset(char_to_reg("C"), 3)  # to

            intel.run_complete_programm(1)

            self.assertEqual(2, intel.registers.get_register_with_offset(char_to_reg("C")))

    def test_mvi_r(self):
        with Intel8080() as intel, i8080asm as asm:
            intel.init("mvi h, 12d")

            intel.run_complete_programm(1)

            self.assertEqual(12, intel.registers.get_register_with_offset(char_to_reg("H")))

    def test_push_rp(self):
        with Intel8080() as intel, i8080asm as asm:
            intel.init("push b")

            intel.registers.set_register8_with_offset(char_to_reg("B"), 2)  # high
            intel.registers.set_register8_with_offset(char_to_reg("C"), 3)  # low
            intel.set_sp(100)

            intel.run_complete_programm(1)

            self.assertEqual(intel.program[100], 2)
            self.assertEqual(intel.program[99], 3)
