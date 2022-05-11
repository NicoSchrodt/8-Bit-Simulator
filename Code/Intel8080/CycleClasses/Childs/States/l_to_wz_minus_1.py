import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class l_to_wz_minus_1(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("l_to_wz_minus_1")
        l_val = self.processor.registers.get_register_with_offset(char_to_reg("L"))
        wz = np.uint16(self.processor.get_wz() - 1)

        self.processor.set_memory_byte(wz, l_val)
        self.processor.StateLogger.addEntry("l_to_wz_minus_1")
