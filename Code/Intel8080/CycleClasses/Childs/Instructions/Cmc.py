from Code.Intel8080.CycleClasses.Childs.MachineCycles.Cmc_M1 import Cmc_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Cmc(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Cmc_M1(processor)]
        pass
