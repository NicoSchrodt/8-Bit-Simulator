from Code.Intel8080.CycleClasses.Childs.States.h_to_wz import h_to_wz
from Code.Intel8080.CycleClasses.Childs.States.wz_out_status import wz_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Shld_M5(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(wz_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(h_to_wz(processor))
