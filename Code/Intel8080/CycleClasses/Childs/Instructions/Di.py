from Code.Intel8080.CycleClasses.Childs.MachineCycles.Di_M1 import Di_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Di(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Di_M1(processor)]
        pass
