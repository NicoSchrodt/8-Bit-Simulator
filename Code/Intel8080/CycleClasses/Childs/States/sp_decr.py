import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class sp_decr(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sp_decr")
        self.processor.set_sp(np.uint16(self.processor.get_sp() - 1))
