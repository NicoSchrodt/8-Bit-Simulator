from Code.Intel8080.CycleClasses.Childs.Instructions.SubParents.Load_store import Load_store
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Lhld_M4 import Lhld_M4
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Lhld_M5 import Lhld_M5


class Lhld(Load_store):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles.append(Lhld_M4(processor))
        self.machine_cycles.append(Lhld_M5(processor))
        pass
