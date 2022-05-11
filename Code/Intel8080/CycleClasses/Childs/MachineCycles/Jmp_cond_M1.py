from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.ccc_is_true import ccc_is_true
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState


class Jmp_cond_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(ccc_is_true(processor))
