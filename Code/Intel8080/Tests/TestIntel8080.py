from unittest import TestCase

import numpy as np

from Code.Intel8080.Intel8080 import Intel8080
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class TestIntel8080(TestCase):

    def test_framework(self):
        self.assertTrue(True)

    def test_aci(self):
        try:
            intel = Intel8080()
            intel.init_test("aci 63")

            intel.set_acc(7)

            intel.run_complete_programm(1)

            self.assertEqual(70, intel.get_acc())
        except:
            self.fail()

    def test_adc_r(self):
        try:
            intel = Intel8080()
            intel.init_test("adc b")

            intel.set_acc(7)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 63)

            intel.run_complete_programm(1)

            self.assertEqual(70, intel.get_acc())
        except:
            self.fail()

    def test_adc_m(self):
        try:
            intel = Intel8080()
            intel.init_test("adc m")

            intel.set_acc(7)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 63

            intel.run_complete_programm(1)

            self.assertEqual(70, intel.get_acc())
        except:
            self.fail()

    def test_add_m(self):
        try:
            intel = Intel8080()
            intel.init_test("add m")

            intel.set_acc(7)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 63

            intel.run_complete_programm(1)

            self.assertEqual(70, intel.get_acc())
        except:
            self.fail()

    def test_add_r(self):
        try:
            intel = Intel8080()
            intel.init_test("add b")

            intel.set_acc(7)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 63)

            intel.run_complete_programm(1)

            self.assertEqual(70, intel.get_acc())
        except:
            self.fail()

    def test_adi(self):
        try:
            intel = Intel8080()
            intel.init_test("adi 63")

            intel.set_acc(7)

            intel.run_complete_programm(1)

            self.assertEqual(70, intel.get_acc())
        except:
            self.fail()

    def test_ana_m(self):
        try:
            intel = Intel8080()
            intel.init_test("ana m")

            intel.set_acc(0xFC)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 0x0F

            intel.run_complete_programm(1)

            self.assertEqual(0x0C, intel.get_acc())
        except:
            self.fail()

    def test_ana_r(self):
        try:
            intel = Intel8080()
            intel.init_test("ana b")  # TODO Fehler "ana d" wird auch zu sss = 000

            intel.set_acc(0xFC)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 0x0F)

            intel.run_complete_programm(1)

            self.assertEqual(0x0C, intel.get_acc())
        except:
            self.fail()

    def test_ani(self):
        try:
            intel = Intel8080()
            intel.init_test("ani 0fh")

            intel.set_acc(0xFC)

            intel.run_complete_programm(1)

            self.assertEqual(0x0C, intel.get_acc())
        except:
            self.fail()

    def test_call(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Di
                                    Loop:
                                        call 11ddh""")

            intel.set_sp(80)

            intel.run_complete_programm(3)

            self.assertEqual(0x11dd, intel.get_pc())
            self.assertEqual(0, intel.program[79])
            self.assertEqual(5, intel.program[78])
        except:
            self.fail()

    def test_call_cond_skip(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Di
                                    Loop:
                                        cc 11ddh""")

            intel.set_sp(80)
            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(3)

            self.assertEqual(5, intel.get_pc())
            self.assertEqual(0, intel.program[79])
            self.assertEqual(0, intel.program[78])
        except:
            self.fail()

    def test_cc(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Di
                                    Loop:
                                        cc 11ddh""")

            intel.ALU.set_carry_flag(True)
            intel.set_sp(80)

            intel.run_complete_programm(3)

            self.assertEqual(0x11dd, intel.get_pc())
            self.assertEqual(0, intel.program[79])
            self.assertEqual(5, intel.program[78])
        except:
            self.fail()

    def test_cnc(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Di
                                    Loop:
                                        cnc 11ddh""")

            intel.ALU.set_carry_flag(False)
            intel.set_sp(80)

            intel.run_complete_programm(3)

            self.assertEqual(0x11dd, intel.get_pc())
            self.assertEqual(0, intel.program[79])
            self.assertEqual(5, intel.program[78])
        except:
            self.fail()

    def test_cma(self):
        try:
            intel = Intel8080()
            intel.init_test("cma")

            intel.set_acc(0x51)

            intel.run_complete_programm(1)

            self.assertEqual(0xAE, intel.get_acc())
        except:
            self.fail()

    def test_cmc(self):
        try:
            intel = Intel8080()
            intel.init_test("cmc")

            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(1)

            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_cmc_2(self):
        try:
            intel = Intel8080()
            intel.init_test("cmc")

            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(1)

            self.assertFalse(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_cmp_m(self):
        try:
            intel = Intel8080()
            intel.init_test("cmp m")

            intel.set_acc(0x0A)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 0x05

            intel.run_complete_programm(1)

            self.assertFalse(intel.ALU.get_zero_flag())
            self.assertFalse(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_cmp_r(self):
        try:
            intel = Intel8080()
            intel.init_test("cmp b")  # (TODO Fehler "xra d" wird auch zu sss = 000)

            intel.set_acc(0x0A)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 0x0A)

            intel.run_complete_programm(1)

            self.assertTrue(intel.ALU.get_zero_flag())
            self.assertFalse(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_cpi(self):
        try:
            intel = Intel8080()
            intel.init_test("cpi 0Bh")

            intel.set_acc(0x0A)

            intel.run_complete_programm(1)

            self.assertFalse(intel.ALU.get_zero_flag())
            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_hlt(self):
        try:
            intel = Intel8080()
            intel.init_test("hlt")

            intel.run_complete_programm(1)

            self.assertTrue(intel.is_halted())
        except:
            self.fail()

    def test_daa(self):
        try:
            intel = Intel8080()
            intel.init_test("daa")

            intel.set_acc(0x9B)

            intel.run_complete_programm(1)

            self.assertEqual(1, intel.get_acc())
            self.assertTrue(intel.ALU.get_auxiliary_carry_flag())
            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_dad(self):
        try:
            intel = Intel8080()
            intel.init_test("dad h")

            intel.registers.set_register8_with_offset(char_to_reg("H"), 22)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 33)

            intel.run_complete_programm(1)

            self.assertEqual(44, intel.registers.get_register_with_offset(char_to_reg("H")))
            self.assertEqual(66, intel.registers.get_register_with_offset(char_to_reg("L")))
        except:
            self.fail()

    def test_dcr_m(self):
        try:
            intel = Intel8080()
            intel.init_test("dcr m")

            intel.program[10] = 55
            intel.registers.set_register8_with_offset(char_to_reg("H"), 0)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(54, intel.program[10])
        except:
            self.fail()

    def test_dcr_r(self):
        try:
            intel = Intel8080()
            intel.init_test("dcr b")

            intel.registers.set_register8_with_offset(char_to_reg("B"), 22)
            intel.run_complete_programm(1)

            self.assertEqual(21, intel.registers.get_register_with_offset(char_to_reg("B")))
        except:
            self.fail()

    def test_dcx(self):
        try:
            intel = Intel8080()
            intel.init_test("dcx b")

            intel.registers.set_register8_with_offset(char_to_reg("C"), 5)
            intel.run_complete_programm(1)

            self.assertEqual(4, intel.registers.get_register_with_offset(char_to_reg("C")))
        except:
            self.fail()

    def test_di(self):
        try:
            intel = Intel8080()
            intel.init_test("di")

            intel.interrupt_enabled = True

            intel.run_complete_programm(1)

            self.assertFalse(intel.interrupt_enabled)
        except:
            self.fail()

    def test_ei(self):
        try:
            intel = Intel8080()
            intel.init_test("ei")

            intel.interrupt_enabled = False

            intel.run_complete_programm(1)

            self.assertTrue(intel.interrupt_enabled)
        except:
            self.fail()

    def test_in(self):
        try:
            intel = Intel8080()
            intel.init_test("in 0Ah")

            intel.run_complete_programm(1)

            self.assertEqual(0x0A, intel.registers.get_register_with_offset(char_to_reg("Z")))
            self.assertEqual(0x0A, intel.registers.get_register_with_offset(char_to_reg("W")))
        except:
            self.fail()

    def test_inr_m(self):
        try:
            intel = Intel8080()
            intel.init_test("inr m")

            intel.program[10] = 55
            intel.registers.set_register8_with_offset(char_to_reg("H"), 0)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(56, intel.program[10])
        except:
            self.fail()

    def test_inr_r(self):
        try:
            intel = Intel8080()
            intel.init_test("inr c")

            intel.registers.set_register8_with_offset(char_to_reg("C"), 5)
            intel.run_complete_programm(1)

            self.assertEqual(6, intel.registers.get_register_with_offset(char_to_reg("C")))
        except:
            self.fail()

    def test_inx(self):
        try:
            intel = Intel8080()
            intel.init_test("inx b")

            intel.registers.set_register8_with_offset(char_to_reg("C"), 5)
            intel.run_complete_programm(1)

            self.assertEqual(6, intel.registers.get_register_with_offset(char_to_reg("C")))
        except:
            self.fail()

    def test_jmp(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Di
                                    Loop:
                                        jmp start""")

            intel.run_complete_programm(3)

            self.assertEqual(0, intel.get_pc())
        except:
            self.fail()

    def test_jmp_cond_skip(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Nop
                                    Loop:
                                        jc start""")

            intel.set_sp(80)
            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(3)

            self.assertEqual(3, intel.get_pc())
        except:
            self.fail()

    def test_jc(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Nop
                                    Loop:
                                        jc start""")

            intel.set_sp(80)
            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(3)

            self.assertEqual(0, intel.get_pc())
        except:
            self.fail()

    def test_jnc(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                                    Start:
                                        Nop
                                        Nop
                                    Loop:
                                        jnc start""")

            intel.set_sp(80)
            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(3)

            self.assertEqual(0, intel.get_pc())
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


    def test_ldax(self):
        try:
            intel = Intel8080()
            intel.init_test("ldax b")

            intel.program[10] = 55
            intel.registers.set_register8_with_offset(char_to_reg("B"), 0)  # high
            intel.registers.set_register8_with_offset(char_to_reg("C"), 10)  # low

            intel.run_complete_programm(1)

            self.assertEqual(55, intel.get_acc())
        except:
            self.fail()

    def test_lhld(self):
        try:
            intel = Intel8080()
            intel.init_test("lhld 0Ah")

            intel.program[10] = 55
            intel.program[11] = 66

            intel.run_complete_programm(1)

            self.assertEqual(55, intel.registers.get_register_with_offset(char_to_reg("L")))
            self.assertEqual(66, intel.registers.get_register_with_offset(char_to_reg("H")))
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

    def test_ora_m(self):
        try:
            intel = Intel8080()
            intel.init_test("ora m")

            intel.set_acc(0xAA)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 0x0F

            intel.run_complete_programm(1)

            self.assertEqual(0xAF, intel.get_acc())
        except:
            self.fail()

    def test_ora_r(self):
        try:
            intel = Intel8080()
            intel.init_test("ora b")  # TODO Fehler "xra d" wird auch zu sss = 000

            intel.set_acc(0xAA)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 0x0F)

            intel.run_complete_programm(1)

            self.assertEqual(0xAF, intel.get_acc())
        except:
            self.fail()

    def test_ori(self):
        try:
            intel = Intel8080()
            intel.init_test("ori 0Fh")

            intel.set_acc(0xAA)

            intel.run_complete_programm(1)

            self.assertEqual(0xAF, intel.get_acc())
        except:
            self.fail()

    def test_out(self):
        try:
            intel = Intel8080()
            intel.init_test("out 0Ah")

            intel.run_complete_programm(1)

            self.assertEqual(0x0A, intel.registers.get_register_with_offset(char_to_reg("Z")))
            self.assertEqual(0x0A, intel.registers.get_register_with_offset(char_to_reg("W")))
        except:
            self.fail()

    def test_pchl(self):
        try:
            intel = Intel8080()
            intel.init_test("pchl")

            intel.registers.set_register8_with_offset(char_to_reg("H"), 0)  # to
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(0x000A, intel.get_pc())
        except:
            self.fail()

    def test_pop_rp(self):
        try:
            intel = Intel8080()
            intel.init_test("pop b")

            intel.program[79] = 3
            intel.program[78] = 2
            intel.set_sp(78)

            intel.run_complete_programm(1)

            self.assertEqual(3, intel.registers.get_register_with_offset(char_to_reg("B")))
            self.assertEqual(2, intel.registers.get_register_with_offset(char_to_reg("C")))
            self.assertEqual(80, intel.get_sp())
        except:
            self.fail()

    def test_pop_psw(self):
        try:
            intel = Intel8080()
            intel.init_test("pop psw")

            intel.program[79] = 3
            intel.program[78] = 0b01000111
            intel.set_sp(78)

            intel.run_complete_programm(1)

            self.assertEqual(3, intel.get_acc())
            self.assertEqual(True, intel.ALU.get_carry_flag())
            self.assertEqual(False, intel.ALU.get_auxiliary_carry_flag())
            self.assertEqual(True, intel.ALU.get_zero_flag())
            self.assertEqual(True, intel.ALU.get_parity_flag())
            self.assertEqual(False, intel.ALU.get_sign_flag())
            self.assertEqual(80, intel.get_sp())
        except:
            self.fail()

    def test_push_psw(self):
        try:
            intel = Intel8080()
            intel.init_test("push psw")

            intel.set_acc(0x55)  # high
            intel.ALU.set_carry_flag(True)
            intel.ALU.set_auxiliary_carry_flag(False)
            intel.ALU.set_zero_flag(True)
            intel.ALU.set_parity_flag(True)
            intel.ALU.set_sign_flag(False)
            intel.set_sp(80)

            intel.run_complete_programm(1)

            self.assertEqual(0x55, intel.program[79])
            self.assertEqual(0b01000111, intel.program[78])
            self.assertEqual(78, intel.get_sp())
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
            self.assertEqual(78, intel.get_sp())
        except:
            self.fail()

    def test_ral(self):
        try:
            intel = Intel8080()
            intel.init_test("ral")

            intel.set_acc(0xAA)
            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(1)

            self.assertEqual(0x55, intel.get_acc())
            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_rar(self):
        try:
            intel = Intel8080()
            intel.init_test("rar")

            intel.set_acc(0xAA)
            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(1)

            self.assertEqual(0xD5, intel.get_acc())
            self.assertFalse(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_rlc(self):
        try:
            intel = Intel8080()
            intel.init_test("rlc")

            intel.set_acc(0xAA)
            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(1)

            self.assertEqual(0x55, intel.get_acc())
            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_rrc(self):
        try:
            intel = Intel8080()
            intel.init_test("rrc")

            intel.set_acc(0xAB)
            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(1)

            self.assertEqual(0xD5, intel.get_acc())
            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_rst(self):
        try:
            intel = Intel8080()
            intel.init_test("rst 3")

            intel.set_sp(80)
            intel.registers.set_register8_with_offset(char_to_reg("W"), 0)

            intel.run_complete_programm(1)

            self.assertEqual(24, intel.get_pc())
            self.assertEqual(78, intel.get_sp())
            self.assertEqual(0, intel.program[79])
            self.assertEqual(1, intel.program[78])
            self.assertEqual(3 << 3, intel.get_tmp())
            self.assertEqual(3 << 3, intel.registers.get_register_with_offset(char_to_reg("Z")))
        except:
            self.fail()

    def test_shld(self):
        try:
            intel = Intel8080()
            intel.init_test("shld 0Ah")

            intel.registers.set_register8_with_offset(char_to_reg("L"), 55)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 66)
            intel.set_sp(80)

            intel.run_complete_programm(1)

            self.assertEqual(55, intel.program[10])
            self.assertEqual(66, intel.program[11])
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

    def test_sta(self):
        try:
            intel = Intel8080()
            intel.init_test("sta 000fh")

            intel.registers.set_register8_with_offset(char_to_reg("A"), 22)

            intel.run_complete_programm(1)

            self.assertEqual(22, intel.get_memory_byte(0x000f))

        except:
            self.fail()

    def test_stax(self):
        try:
            intel = Intel8080()
            intel.init_test("stax b")

            intel.set_acc(22)

            intel.registers.set_register8_with_offset(char_to_reg("B"), 0)
            intel.registers.set_register8_with_offset(char_to_reg("C"), 10)

            intel.run_complete_programm(1)

            self.assertEqual(22, intel.get_memory_byte(10))

        except:
            self.fail()

    def test_stc(self):
        try:
            intel = Intel8080()
            intel.init_test("stc")

            intel.ALU.set_carry_flag(False)

            intel.run_complete_programm(1)

            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_stc_2(self):
        try:
            intel = Intel8080()
            intel.init_test("stc")

            intel.ALU.set_carry_flag(True)

            intel.run_complete_programm(1)

            self.assertTrue(intel.ALU.get_carry_flag())
        except:
            self.fail()

    def test_sbb_r(self):
        try:
            intel = Intel8080()
            intel.init_test("sbb b")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 63)

            intel.run_complete_programm(1)

            self.assertEqual(7, intel.get_acc())
        except:
            self.fail()

    def test_sbb_m(self):
        try:
            intel = Intel8080()
            intel.init_test("sub m")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 63

            intel.run_complete_programm(1)

            self.assertEqual(7, intel.get_acc())
        except:
            self.fail()

    def test_sbi(self):
        try:
            intel = Intel8080()
            intel.init_test("sui 63")

            intel.set_acc(70)

            intel.run_complete_programm(1)

            self.assertEqual(7, intel.get_acc())
        except:
            self.fail()

    def test_sub_r(self):
        try:
            intel = Intel8080()
            intel.init_test("sub b")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 63)

            intel.run_complete_programm(1)

            self.assertEqual(7, intel.get_acc())
        except:
            self.fail()

    def test_sub_m(self):
        try:
            intel = Intel8080()
            intel.init_test("sub m")

            intel.set_acc(70)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 63

            intel.run_complete_programm(1)

            self.assertEqual(7, intel.get_acc())
        except:
            self.fail()

    def test_sui(self):
        try:
            intel = Intel8080()
            intel.init_test("sui 63")

            intel.set_acc(70)

            intel.run_complete_programm(1)

            self.assertEqual(7, intel.get_acc())
        except:
            self.fail()

    def test_xchg(self):
        try:
            intel = Intel8080()
            intel.init_test("xchg")

            intel.registers.set_register8_with_offset(char_to_reg("H"), 22)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 33)
            intel.registers.set_register8_with_offset(char_to_reg("D"), 44)
            intel.registers.set_register8_with_offset(char_to_reg("E"), 55)

            intel.run_complete_programm(1)

            self.assertEqual(22, intel.registers.get_register_with_offset(char_to_reg("D")))
            self.assertEqual(33, intel.registers.get_register_with_offset(char_to_reg("E")))
            self.assertEqual(44, intel.registers.get_register_with_offset(char_to_reg("H")))
            self.assertEqual(55, intel.registers.get_register_with_offset(char_to_reg("L")))
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

    def test_xra_r(self):
        try:
            intel = Intel8080()
            intel.init_test("xra b")  # TODO Fehler "xra d" wird auch zu sss = 000

            intel.set_acc(0xAA)
            intel.registers.set_register8_with_offset(char_to_reg("B"), 0x0F)

            intel.run_complete_programm(1)

            self.assertEqual(0xA5, intel.get_acc())
        except:
            self.fail()

    def test_xra_m(self):
        try:
            intel = Intel8080()
            intel.init_test("xra m")

            intel.set_acc(0xAA)
            intel.registers.set_register8_with_offset(char_to_reg("H"), 00)
            intel.registers.set_register8_with_offset(char_to_reg("L"), 10)
            intel.program[10] = 0x0F

            intel.run_complete_programm(1)

            self.assertEqual(0xA5, intel.get_acc())
        except:
            self.fail()

    def test_xri(self):
        try:
            intel = Intel8080()
            intel.init_test("xri 0Fh")

            intel.set_acc(0xAA)

            intel.run_complete_programm(1)

            self.assertEqual(0xA5, intel.get_acc())
        except:
            self.fail()
