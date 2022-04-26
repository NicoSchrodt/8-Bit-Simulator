from Code.Intel8080.CycleClasses.Childs.States.h_to_sp import h_to_sp
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Xthl_M4(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(FetchState1(processor))
        self.states.append(EmptyState(processor))
        self.states.append(h_to_sp(processor))
