from Code.Intel8080.CycleClasses.Childs.MachineCycles.Cond_M1 import Cond_M1

from Code.Intel8080.CycleClasses.Childs.MachineCycles.Jmp_M3 import Jmp_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Write_z import Write_z
from Code.Intel8080.CycleClasses.Childs.MachineCycles.wz_to_pc_mc import wz_to_pc_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Jmp_cond(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Cond_M1(processor),
                               Write_z(processor),
                               Jmp_M3(processor),
                               wz_to_pc_mc(processor)]
        pass
