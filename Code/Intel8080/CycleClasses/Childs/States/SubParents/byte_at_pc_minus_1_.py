import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class byte_at_pc_minus_1_(State):
    def __init__(self, processor):
        super().__init__(processor)
        self.byte = np.uint8(0)

    def run(self):
        self.set_b2()
        self.write_to()

    def set_b2(self):
        self.byte = self.processor.get_memory_byte(np.uint16(self.processor.get_pc() - 1))

    def write_to(self):
        pass
