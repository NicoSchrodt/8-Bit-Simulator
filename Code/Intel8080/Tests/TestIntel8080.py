from unittest import TestCase

from Code.Intel8080.CycleClasses.Childs.Mov_r_r import Mov_r_r
from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class TestIntel8080(TestCase):

    def test_framework(self):
        self.assertTrue(True)

    def test_Mov_r_r(self):
        intel = Intel8080()
        intel.init("mov c, b")

        intel.registers.set_register8_with_offset(char_to_reg("B"), 2)  # from
        intel.registers.set_register8_with_offset(char_to_reg("C"), 3)  # to

        intel.run_complete_programm(1)

        self.assertEqual(intel.registers.get_register_with_offset(char_to_reg("C")), 2)
