from Code.Intel8080.CycleClasses.Childs.MachineCycles.Push_M1 import Push_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Push_rp_M2 import Push_rp_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Push_rp_M3 import Push_rp_M3
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Push_rp(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Push_M1(processor),
                               Push_rp_M2(processor),
                               Push_rp_M3(processor)]
        pass
