from Code.Intel8080.CycleClasses.Childs.MachineCycles.Rrc_M1 import Rrc_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.alu_to_a_and_cy_mc import alu_to_a_and_cy_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Rrc(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Rrc_M1(processor),
                               alu_to_a_and_cy_mc(processor)]
        pass
