from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mov_r_m_M2 import Mov_r_m_M2
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Mov_r_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Mov_r_m_M2(processor)]
        pass
