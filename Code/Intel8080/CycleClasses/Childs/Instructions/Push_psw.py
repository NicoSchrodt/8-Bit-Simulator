from Code.Intel8080.CycleClasses.Childs.MachineCycles.Push_M1 import Push_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Push_psw_M2 import Push_psw_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Push_psw_M3 import Push_psw_M3
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Push_psw(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Push_M1(processor),
                               Push_psw_M2(processor),
                               Push_psw_M3(processor)]
        pass
