import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class byte_at_pc_(State):
    def __init__(self, processor):
        super().__init__(processor)
        self.byte = np.uint8(0)

    def run(self):
        self.set_b2()
        self.write_to()

    def set_b2(self):
        self.byte = self.processor.get_byte_from_memory_address_at_pc()

    def write_to(self):
        pass
