import numpy as np

from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class nnn_to_z_and_pcl_to_sp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("nnn_to_z_and_pcl_to_sp_plus_1")
        nnn = self.processor.get_nnn()
        nnn = nnn << 3
        self.processor.set_tmp(nnn)
        self.processor.registers.set_register8_with_offset(char_to_reg("Z"), nnn)

        pcl = np.uint8(self.processor.get_pc() & 0x00FF)
        self.processor.set_memory_byte(self.processor.get_sp(), pcl)
