from Code.Intel8080.CycleClasses.Childs.MachineCycles.Dad_M2 import Dad_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Dad_M3 import Dad_M3
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Dad(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Dad_M2(processor),
                               Dad_M3(processor)]
        pass
