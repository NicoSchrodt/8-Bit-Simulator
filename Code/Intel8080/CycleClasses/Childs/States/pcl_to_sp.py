import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class pcl_to_sp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("pcl_to_sp")
        pcl = np.uint8(self.processor.get_pc() & 0x00FF)
        self.processor.set_memory_byte(self.processor.get_sp(), pcl)
