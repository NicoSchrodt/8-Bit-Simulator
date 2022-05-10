from Code.Intel8080.CycleClasses.Childs.MachineCycles.Ldax_M2 import Ldax_M2
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Ldax(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Ldax_M2(processor)]
        pass
