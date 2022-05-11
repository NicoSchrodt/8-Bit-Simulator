from Code.Intel8080.CycleClasses.Childs.MachineCycles.Stc_M1 import Stc_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Stc(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Stc_M1(processor)]
        pass
