from Code.Intel8080.CycleClasses.Childs.States.sp_to_w import sp_to_w
from Code.Intel8080.CycleClasses.Childs.States.sp_plus_1 import sp_plus_1
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Xthl_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(FetchState1(processor))
        self.states.append(EmptyState(processor))
        self.states.append(sp_to_w(processor))
