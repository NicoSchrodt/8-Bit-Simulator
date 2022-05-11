from Code.Intel8080.CycleClasses.Childs.MachineCycles.Rst_M1 import Rst_M1
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Rst_M2 import Rst_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Rst_M3 import Rst_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.wz_to_pc_mc import wz_to_pc_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Rst(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Rst_M1(processor),
                               Rst_M2(processor),
                               Rst_M3(processor),
                               wz_to_pc_mc(processor)]
        pass
