import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class wz_incr(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("wz_incr")
        wz = self.processor.get_wz()
        wz = np.uint16(wz + 1)
        self.processor.set_wz(wz)
