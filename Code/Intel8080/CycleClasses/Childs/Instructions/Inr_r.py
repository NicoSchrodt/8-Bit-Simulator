from Code.Intel8080.CycleClasses.Childs.MachineCycles.Inr_r_M1 import Inr_r_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Inr_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Inr_r_M1(processor)]  # TODO Flags setzen
        pass
