from Code.Intel8080.CycleClasses.Childs.States.acc_to_mem import acc_to_mem
from Code.Intel8080.CycleClasses.Childs.States.wz_out_status import wz_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Sta_M4(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(wz_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(acc_to_mem(processor))
