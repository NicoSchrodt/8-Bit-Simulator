from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.ccc_if_true_then_sp_decr import ccc_if_true_then_sp_decr
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState


class Call_cond_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(ccc_if_true_then_sp_decr(processor))
