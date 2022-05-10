from Code.Intel8080.CycleClasses.Childs.Instructions.SubParents.Load_store import Load_store
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Sta_M4 import Sta_M4


class Sta(Load_store):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles.append(Sta_M4(processor))
        pass
