from Code.Intel8080.CycleClasses.Childs.Instructions.SubParents.Load_store import Load_store
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Lda_M4 import Lda_M4


class Lda(Load_store):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles.append(Lda_M4(processor))
        pass
