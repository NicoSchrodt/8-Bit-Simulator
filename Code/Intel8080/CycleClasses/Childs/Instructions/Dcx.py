from Code.Intel8080.CycleClasses.Childs.MachineCycles.Dcx_M1 import Dcx_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Dcx(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Dcx_M1(processor)]
        pass
