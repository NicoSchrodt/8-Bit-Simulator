from Code.Intel8080.CycleClasses.Childs.MachineCycles.Ei_M1 import Ei_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Ei(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Ei_M1(processor)]
        pass
