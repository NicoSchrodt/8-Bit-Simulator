from Code.Intel8080.CycleClasses.Childs.MachineCycles.Jmp_M1 import Jmp_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Jmp_M2 import Jmp_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Jmp_M3 import Jmp_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Jmp_M5 import Jmp_M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Jmp(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Jmp_M1(processor), Jmp_M2(processor),
                               Jmp_M3(processor), Jmp_M5(processor)]
        pass
