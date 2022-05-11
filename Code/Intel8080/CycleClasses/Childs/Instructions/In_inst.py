from Code.Intel8080.CycleClasses.Childs.MachineCycles.In_M3 import In_M3
from Code.Intel8080.CycleClasses.Childs.MachineCycles.in_out_mc import in_out_mc
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class In_inst(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               in_out_mc(processor),
                               In_M3(processor)]
        pass
