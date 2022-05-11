import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class pch_to_sp_plus_1(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("pch_to_sp_plus_1")
        pch = np.uint8((self.processor.get_pc() & 0xFF00) >> 8)
        self.processor.set_memory_byte(self.processor.get_sp() + 1, pch)
        self.processor.StateLogger.addEntry("pch_to_sp_plus_1")
