from Code.Intel8080.CycleClasses.Childs.MachineCycles.Cma_M1 import Cma_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Cma(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Cma_M1(processor)]
        pass
