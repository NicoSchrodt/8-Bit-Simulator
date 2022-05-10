from Code.Intel8080.CycleClasses.Childs.Instructions.SubParents.Load_store import Load_store
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Shld_M4 import Shld_M4
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Shld_M5 import Shld_M5


class Shld(Load_store):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles.append(Shld_M4(processor))
        self.machine_cycles.append(Shld_M5(processor))
        pass
