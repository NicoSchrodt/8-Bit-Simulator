import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class cmp_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("cmp_state")
        act = self.processor.get_act()
        tmp = self.processor.get_tmp()

        ac, cy, result = self.processor.ALU.binary_sub(act, tmp)

        self.processor.ALU.set_carry_flag(result >= 127)
        self.processor.ALU.set_zero_flag(result == 0)

        self.processor.ALU.evaluate_zsp_flags(False, True, True, result)
        self.processor.ALU.set_auxiliary_carry_flag(ac)
