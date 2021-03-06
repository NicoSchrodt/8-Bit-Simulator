import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class tmp_minus_1_to_ddd(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("tmp_minus_1_to_ddd")
        ac, cy, result = self.processor.ALU.binary_sub(self.processor.get_tmp(), 1)
        result = np.uint8(result)
        self.processor.ALU.evaluate_zsp_flags(True, True, True, result)
        self.processor.ALU.set_auxiliary_carry_flag(ac)
        self.processor.set_ddd(result)
        self.processor.StateLogger.addEntry("tmp_minus_1_to_ddd")
