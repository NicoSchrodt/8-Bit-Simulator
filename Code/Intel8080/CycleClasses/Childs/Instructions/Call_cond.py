from Code.Intel8080.CycleClasses.Childs.MachineCycles.Call_M4 import Call_M4
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Call_M5 import Call_M5
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Call_cond_M1 import Call_cond_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Call_cond_M3 import Call_cond_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Write_z import Write_z
from Code.Intel8080.CycleClasses.Childs.MachineCycles.wz_to_pc_mc import wz_to_pc_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Call_cond(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Call_cond_M1(processor),
                               Write_z(processor),
                               Call_cond_M3(processor),
                               Call_M4(processor),
                               Call_M5(processor),
                               wz_to_pc_mc(processor)]
        pass
