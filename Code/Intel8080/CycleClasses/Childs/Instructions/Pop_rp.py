from Code.Intel8080.CycleClasses.Childs.MachineCycles.Pop_rp_M2 import Pop_rp_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Pop_rp_M3 import Pop_rp_M3
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Pop_rp(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Pop_rp_M2(processor),
                               Pop_rp_M3(processor)]
        pass
