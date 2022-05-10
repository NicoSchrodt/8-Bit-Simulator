import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class wz_minus_1_to_l(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("wz_minus_1_to_l")
        wz = self.processor.get_wz()
        wz = np.uint16(wz - 1)

        wz_val = self.processor.get_memory_byte(wz)
        self.processor.registers.set_register8_with_offset(char_to_reg("L"), wz_val)
