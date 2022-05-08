import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg, build_16bit_from_8bit


class wz_plus_1_to_pc(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("wz_plus_1_to_pc")
        w_val = self.processor.registers.get_register_with_offset(char_to_reg("W"))
        z_val = self.processor.registers.get_register_with_offset(char_to_reg("Z"))
        new_pc = np.uint16(build_16bit_from_8bit(w_val, z_val) + 1)
        self.processor.set_pc(new_pc)
