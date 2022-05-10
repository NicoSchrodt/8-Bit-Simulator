from Code.Intel8080.CycleClasses.Childs.MachineCycles.Stax_M2 import Stax_M2
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Stax(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Stax_M2(processor)]
        pass
