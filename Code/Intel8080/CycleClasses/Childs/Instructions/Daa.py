from Code.Intel8080.CycleClasses.Childs.MachineCycles.Daa_M1 import Daa_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Daa(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Daa_M1(processor)]
        pass
