import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State


class data_to_(State):
    def __init__(self, processor):
        super().__init__(processor)
        self.data = np.uint8(0)

    def run(self):
        self.set_data()
        self.write_to()

    def set_data(self):
        self.data = self.processor.get_h_l_value()

    def write_to(self):
        pass
