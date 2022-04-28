from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mov_r_m_M1 import Mov_r_m_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mov_r_m_M2 import Mov_r_m_M2
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Mov_r_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Mov_r_m_M1(processor), Mov_r_m_M2(processor)]
        pass
