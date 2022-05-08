from Code.Intel8080.CycleClasses.Childs.MachineCycles.Lxi_M2 import Lxi_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Lxi_M3 import Lxi_M3
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Lxi(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Lxi_M2(processor),
                               Lxi_M3(processor)]
        pass
