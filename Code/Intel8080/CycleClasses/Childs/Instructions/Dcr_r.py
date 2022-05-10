from Code.Intel8080.CycleClasses.Childs.MachineCycles.Dcr_r_M1 import Dcr_r_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Dcr_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Dcr_r_M1(processor)]
        pass
