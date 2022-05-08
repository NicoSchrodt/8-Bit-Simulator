from Code.Intel8080.CycleClasses.Childs.MachineCycles.Sphl_M1 import Sphl_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Sphl(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Sphl_M1(processor)]
        pass
