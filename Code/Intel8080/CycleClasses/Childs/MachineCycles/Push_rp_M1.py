from Code.Intel8080.CycleClasses.Childs.States.sp_minus_1 import sp_minus_1
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Fetch import Fetch


class Push_rp_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(sp_minus_1(processor))
