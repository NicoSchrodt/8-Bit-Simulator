from Code.Intel8080.CycleClasses.Childs.MachineCycles.Rar_M1 import Rar_M1

from Code.Intel8080.CycleClasses.Childs.MachineCycles.alu_to_a_and_cy_mc import alu_to_a_and_cy_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Rar(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Rar_M1(processor),
                               alu_to_a_and_cy_mc(processor)]
        pass
