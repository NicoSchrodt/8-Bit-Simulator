from Code.Intel8080.CycleClasses.Childs.MachineCycles.Pchl_M1 import Pchl_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Pchl(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Pchl_M1(processor)]
        pass
