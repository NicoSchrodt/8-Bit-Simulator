import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import build_16bit_from_8bit


class rp_incr(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("rp_incr")
        rp = self.processor.get_current_rp()

        if self.processor.rp_means_sp():
            sp = self.processor.get_sp()
            sp = np.uint16(sp + 1)
            self.processor.set_sp(sp)
        else:
            h_val, l_val = self.processor.get_rp_values(rp)
            hl_val = build_16bit_from_8bit(h_val, l_val)
            hl_val = np.uint16(hl_val + 1)
            self.processor.registers.set_2_8bit_reg_with_offset(rp * 2, hl_val)
