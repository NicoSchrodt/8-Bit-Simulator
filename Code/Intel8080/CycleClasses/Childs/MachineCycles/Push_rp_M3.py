from Code.Intel8080.CycleClasses.Childs.States.rl_mem import rl_mem
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Push_rp_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(FetchState1(processor))
        self.states.append(EmptyState(processor))
        self.states.append(rl_mem(processor))
