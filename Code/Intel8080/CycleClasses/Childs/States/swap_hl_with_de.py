from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg, build_16bit_from_8bit


class swap_hl_with_de(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("swap_hl_with_de")
        hl_val = self.processor.get_h_l_address()

        d_val, e_val = self.processor.get_rp_values(1)
        de_val = build_16bit_from_8bit(d_val, e_val)

        self.processor.registers.set_2_8bit_reg_with_offset(char_to_reg("H"), de_val)
        self.processor.registers.set_2_8bit_reg_with_offset(char_to_reg("D"), hl_val)
