import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class ral_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("ral_state")
        acc = self.processor.get_acc()
        self.processor.ALU.set_alu_cy((acc & 0x80) == 0x80)
        acc = np.uint8((acc << 1) + self.processor.ALU.get_carry_flag())
        self.processor.ALU.set_alu(acc)
