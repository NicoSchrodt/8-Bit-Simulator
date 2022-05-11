import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class daa_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("daa_state")
        ac = self.processor.ALU.get_auxiliary_carry_flag()
        cy = self.processor.ALU.get_carry_flag()
        low = self.processor.get_acc() & 0x0f

        if ac or low > 9:
            ac, wrong_cy, result = self.processor.ALU.binary_add(self.processor.get_acc(), 6, 0)
            self.processor.set_acc(np.uint8(result))

        high = self.processor.get_acc() & 0xf0
        if cy or high > 9:
            wrong_ac, cy, result = self.processor.ALU.binary_add(self.processor.get_acc(), 6 << 4, 0)
            self.processor.set_acc(np.uint8(result))

        self.processor.ALU.set_auxiliary_carry_flag(ac)
        self.processor.ALU.set_carry_flag(cy)
        self.processor.ALU.evaluate_zsp_flags(True, True, True, self.processor.get_acc())
        self.processor.StateLogger.addEntry("daa_state")
