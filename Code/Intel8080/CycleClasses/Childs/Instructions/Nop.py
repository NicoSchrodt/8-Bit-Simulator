from Code.Intel8080.CycleClasses.Childs.MachineCycles.Nop_M1 import M1Nop
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Nop(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [M1Nop(processor)]
        pass
