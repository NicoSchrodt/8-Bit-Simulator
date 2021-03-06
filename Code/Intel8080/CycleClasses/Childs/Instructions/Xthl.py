from Code.Intel8080.CycleClasses.Childs.MachineCycles.sp_minus_1_to_z_mc import sp_minus_1_to_z_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Xthl_M3 import Xthl_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Xthl_M4 import Xthl_M4
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Xthl_M5 import Xthl_M5
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Xthl(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               sp_minus_1_to_z_mc(processor),
                               Xthl_M3(processor),
                               Xthl_M4(processor),
                               Xthl_M5(processor)]
        pass
