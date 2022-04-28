from Code.Intel8080.CycleClasses.Childs.States.hl_out_status import hl_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Mov_r_m_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(hl_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append((processor))
