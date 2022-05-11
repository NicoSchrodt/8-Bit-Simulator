from unittest import TestCase

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class ProgramTests(TestCase):

    def test_mvi(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                              mvi b, 20
                              mvi c, 30
                              mov a, b
                              add c
                            """)

            intel.run_complete_programm(4)

            self.assertEqual(50, intel.get_acc())
        except:
            self.fail()

    def test_sbb_r_carry(self):
        try:
            intel = Intel8080()
            intel.init_test("sbb l")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 63)
            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(1)

            self.assertEqual(6, intel.get_acc())
            self.assertTrue(intel.ALU.get_carry_flag())
            self.assertFalse(intel.ALU.get_auxiliary_carry_flag())
            self.assertFalse(intel.ALU.get_zero_flag())
            self.assertFalse(intel.ALU.get_sign_flag())
            self.assertTrue(intel.ALU.get_parity_flag())
        except:
            self.fail()

    def test_sbb_r_zero(self):
        try:
            intel = Intel8080()
            intel.init_test("sbb l")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 70)
            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(1)

            self.assertEqual(0, intel.get_acc())
            self.assertTrue(intel.ALU.get_carry_flag())
            self.assertTrue(intel.ALU.get_auxiliary_carry_flag())
            self.assertTrue(intel.ALU.get_zero_flag())
            self.assertFalse(intel.ALU.get_sign_flag())
            self.assertTrue(intel.ALU.get_parity_flag())
        except:
            self.fail()

    def test_sbb_r_sign(self):
        try:
            intel = Intel8080()
            intel.init_test("sbb l")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 70)
            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(1)

            self.assertEqual(255, intel.get_acc())
            self.assertFalse(intel.ALU.get_carry_flag())
            self.assertFalse(intel.ALU.get_auxiliary_carry_flag())
            self.assertFalse(intel.ALU.get_zero_flag())
            self.assertTrue(intel.ALU.get_sign_flag())
            self.assertFalse(intel.ALU.get_parity_flag())
        except:
            self.fail()
