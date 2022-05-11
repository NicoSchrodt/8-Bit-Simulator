from Code.Intel8080.CycleClasses.Childs.States.sp_decr import sp_decr
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch


class Push_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(sp_decr(processor))
