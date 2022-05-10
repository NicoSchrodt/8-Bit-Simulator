from Code.Intel8080.CycleClasses.Childs.MachineCycles.Sta_M4 import Sta_M4
from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Write_w import Write_w
from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Write_z import Write_z
from Code.Intel8080.CycleClasses.Parents.EmptyM4M5 import EmptyM4M5
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Load_store(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [EmptyM4M5(processor),
                               Write_z(processor),
                               Write_w(processor)]
        pass
