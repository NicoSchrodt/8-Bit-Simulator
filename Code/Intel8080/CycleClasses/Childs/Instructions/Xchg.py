from Code.Intel8080.CycleClasses.Childs.MachineCycles.Xchg_M1 import Xchg_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Xchg(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Xchg_M1(processor)]
        pass
