import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class rrc_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("rrc_state")
        acc = self.processor.get_acc()
        self.processor.ALU.set_alu_cy((acc & 0x01) == 0x01)
        acc = np.uint8((acc >> 1) + (self.processor.ALU.get_alu_cy() * 0x80))
        self.processor.ALU.set_alu(acc)
        self.processor.StateLogger.addEntry("rrc_state")
