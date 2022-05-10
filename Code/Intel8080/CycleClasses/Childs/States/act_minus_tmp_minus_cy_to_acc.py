import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class act_minus_tmp_minus_cy_to_acc(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("act_minus_tmp_minus_cy_to_acc")
        act = self.processor.get_act()
        tmp = self.processor.get_tmp()
        tmp = np.uint8(tmp + self.processor.ALU.get_carry_flag())

        ac, cy, result = self.processor.ALU.binary_sub(act, tmp)
        self.processor.ALU.set_cy_ac_flags(cy, ac)
        self.processor.ALU.evaluate_zsp_flags(True, True, True, result)
        self.processor.set_acc(result)
