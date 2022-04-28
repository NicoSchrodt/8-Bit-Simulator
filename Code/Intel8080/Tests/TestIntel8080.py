from unittest import TestCase

import numpy as np

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class TestIntel8080(TestCase):

    def test_framework(self):
        self.assertTrue(True)

    def test_jmp(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                        Nop
                        Nop
                        Loop:
                            jmp Loop""")

            intel.run_complete_programm(3)

            self.assertEqual(3, intel.get_pc())
        except:
            self.fail()

    def test_Mov_r_r(self):
        try:
            intel = Intel8080()
            intel.init_test("mov c, b")

            intel.registers.set_register8_with_offset(char_to_reg("B"), 2)  # from
            intel.registers.set_register8_with_offset(char_to_reg("C"), 3)  # to

            intel.run_complete_programm(1)

            self.assertEqual(2, intel.registers.get_register_with_offset(char_to_reg("C")))
        except:
            self.fail()

    # def test_Mov_r_m(self):
    #     try:
    #         intel = Intel8080()
    #         intel.init_test("""start:
    #         mov c, start""")
    #
    #         intel.run_complete_programm(1)
    #
    #         # self.assertEqual(2, intel.registers.get_register_with_offset(char_to_reg("C")))
    #     except:
    #         self.fail()

    def test_mvi_r(self):
        try:
            intel = Intel8080()
            intel.init_test("mvi h, 12d")

            intel.next_instruction()

            self.assertEqual(12, intel.registers.get_register_with_offset(char_to_reg("H")))
        except:
            self.fail()

    def test_push_rp(self):
        try:
            intel = Intel8080()
            intel.init_test("push b")

            intel.registers.set_register8_with_offset(char_to_reg("B"), 2)  # high
            intel.registers.set_register8_with_offset(char_to_reg("C"), 3)  # low
            intel.set_sp(80)

            intel.run_complete_programm(1)

            self.assertEqual(intel.program[79], 2)
            self.assertEqual(intel.program[78], 3)
        except:
            self.fail()


    def test_xthl(self):
        try:
            intel = Intel8080()
            intel.init_test("xthl")

            intel.registers.set_register8_with_offset(char_to_reg("H"), 22)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 33)
            intel.set_memory_byte(np.uint16(80), 2)
            intel.set_memory_byte(np.uint16(79), 3)
            intel.set_sp(79)

            intel.run_complete_programm(1)

            self.assertEqual(intel.program[80], 22)
            self.assertEqual(intel.program[79], 33)
            self.assertEqual(intel.registers.get_register_with_offset(char_to_reg("H")), 2)
            self.assertEqual(intel.registers.get_register_with_offset(char_to_reg("L")), 3)
        except:
            self.fail()
