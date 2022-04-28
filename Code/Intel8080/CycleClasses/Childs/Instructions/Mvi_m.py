from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mvi_m_M1 import Mvi_m_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mvi_m_M2 import Mvi_m_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Mvi_m_M3 import Mvi_m_M3
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Mvi_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Mvi_m_M1(processor), Mvi_m_M2(processor), Mvi_m_M3(processor)]
        pass
