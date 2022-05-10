from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.rp_incr import rp_incr
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState


class Inx_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(rp_incr(processor))
