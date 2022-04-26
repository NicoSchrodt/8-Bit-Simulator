from Code.Intel8080.CycleClasses.Childs.States.l_to_sp_minus_1__wz_to_hl import l_to_sp_minus_1__wz_to_hl
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Xthl_M5(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(FetchState1(processor))
        self.states.append(EmptyState(processor))
        self.states.append(l_to_sp_minus_1__wz_to_hl(processor))
