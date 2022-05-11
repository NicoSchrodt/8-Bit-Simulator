import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class tmp_incr(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("tmp_incr")
        tmp = np.uint8(self.processor.get_tmp() + 1)
        self.processor.set_tmp(tmp)
        self.processor.StateLogger.addEntry("tmp_incr")
