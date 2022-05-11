import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class act_plus_tmp_plus_cy_to_h(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("act_plus_tmp_plus_cy_to_h")
        act = self.processor.get_act()
        tmp = self.processor.get_tmp()
        cy = self.processor.ALU.get_carry_flag()

        ac, cy, result = self.processor.ALU.binary_add(act, tmp, cy)
        result = np.uint8(result)
        self.processor.ALU.set_carry_flag(cy)
        self.processor.registers.set_register8_with_offset(char_to_reg("H"), result)
        self.processor.StateLogger.addEntry("act_plus_tmp_plus_cy_to_h")
