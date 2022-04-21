from Code.Intel8080.CycleClasses.Childs.M1Mov import M1Mov
from Code.Intel8080.CycleClasses.Childs.M2Mov import M2Mov
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Mov(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [M1Mov(processor), M2Mov(processor)]
        pass
