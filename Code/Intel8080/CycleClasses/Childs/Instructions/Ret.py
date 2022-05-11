from Code.Intel8080.CycleClasses.Childs.MachineCycles.Ret_M3 import Ret_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.sp_minus_1_to_z_mc import sp_minus_1_to_z_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.wz_to_pc_mc import wz_to_pc_mc
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Ret(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               sp_minus_1_to_z_mc(processor),
                               Ret_M3(processor),
                               wz_to_pc_mc(processor)]
        pass
