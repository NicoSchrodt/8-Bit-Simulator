from Code.Intel8080.CycleClasses.Childs.MachineCycles.Interrupt_M1 import Interrupt_M1
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Interrupt(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Interrupt_M1(processor)]
        pass
