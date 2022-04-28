from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mvi_r_M2 import Mvi_r_M2
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Mvi_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Mvi_r_M2(processor)]
        pass
