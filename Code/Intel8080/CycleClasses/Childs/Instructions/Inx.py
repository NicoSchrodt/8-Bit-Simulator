from Code.Intel8080.CycleClasses.Childs.MachineCycles.Inx_M1 import Inx_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Inx(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Inx_M1(processor)]
        pass
