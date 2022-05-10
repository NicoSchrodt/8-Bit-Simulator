from Code.Intel8080.CycleClasses.Childs.MachineCycles.Inr_m_M2 import Inr_m_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Inr_m_M3 import Inr_m_M3
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Inr_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Inr_m_M2(processor),
                               Inr_m_M3(processor)]
        pass
