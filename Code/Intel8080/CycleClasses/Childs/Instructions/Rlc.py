from Code.Intel8080.CycleClasses.Childs.MachineCycles.Rlc_M1 import Rlc_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.alu_to_a_and_cy_mc import alu_to_a_and_cy_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Rlc(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Rlc_M1(processor),
                               alu_to_a_and_cy_mc(processor)]
        pass
