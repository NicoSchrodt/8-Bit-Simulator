from unittest import TestCase

import numpy as np

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class TestIntel8080(TestCase):

    def test_framework(self):
        self.assertTrue(True)

    def test_hlt(self):
        try:
            intel = Intel8080()
            intel.init_test("hlt")

            intel.run_complete_programm(1)

            self.assertTrue(intel.is_halted())
        except:
            self.fail()

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

    def test_lda(self):
        try:
            intel = Intel8080()
            intel.init_test("lda 0Ah")

            intel.program[10] = 55

            intel.run_complete_programm(1)

            self.assertEqual(55, intel.get_acc())
        except:
            self.fail()

    def test_lxi(self):
        try:
            intel = Intel8080()
            intel.init_test("""Nop
                        label:
                        lxi b, label""")

            intel.run_complete_programm(2)

            self.assertEqual(1, intel.registers.get_register_with_offset(char_to_reg("B")))
            self.assertEqual(0, intel.registers.get_register_with_offset(char_to_reg("C")))
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

    def test_Mov_r_m(self):
        try:
            intel = Intel8080()
            intel.init_test("mov b, m")

            intel.program[10] = 55  # from

            intel.registers.set_register8_with_offset(char_to_reg("H"), 0)  # to
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(55, intel.registers.get_register_with_offset(char_to_reg("B")))
        except:
            self.fail()

    def test_Mov_m_r(self):
        try:
            intel = Intel8080()
            intel.init_test("mov m, b")

            intel.registers.set_register8_with_offset(char_to_reg("B"), 55)  # from

            intel.registers.set_register8_with_offset(char_to_reg("H"), 0)  # to
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(55, intel.program[10])
        except:
            self.fail()

    def test_mvi_r(self):
        try:
            intel = Intel8080()
            intel.init_test("mvi b, 12d")

            intel.run_complete_programm(1)

            self.assertEqual(12, intel.registers.get_register_with_offset(char_to_reg("B")))
        except:
            self.fail()

    def test_mvi_m(self):
        try:
            intel = Intel8080()
            intel.init_test("mvi m, 12d")

            intel.registers.set_register8_with_offset(char_to_reg("H"), 0)  # to
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(12, intel.program[10])
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

            self.assertEqual(2, intel.program[79])
            self.assertEqual(3, intel.program[78])
        except:
            self.fail()

    def test_sphl(self):
        try:
            intel = Intel8080()
            intel.init_test("sphl")

            intel.registers.set_register8_with_offset(char_to_reg("H"), 2)  # high
            intel.registers.set_register8_with_offset(char_to_reg("L"), 3)  # low
            intel.set_sp(80)

            intel.run_complete_programm(1)

            self.assertEqual((2 << 8) + 3, intel.get_sp())
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

            self.assertEqual(22, intel.program[80])
            self.assertEqual(33, intel.program[79])
            self.assertEqual(2, intel.registers.get_register_with_offset(char_to_reg("H")))
            self.assertEqual(3, intel.registers.get_register_with_offset(char_to_reg("L")))
        except:
            self.fail()
