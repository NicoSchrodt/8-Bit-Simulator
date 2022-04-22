from Code.Intel8080.CycleClasses.Childs.M1Mov_r_r import M1Mov_r_r
from Code.Intel8080.CycleClasses.Childs.M2Mov import M2Mov
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Mov_r_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [M1Mov_r_r(processor)]
        pass
