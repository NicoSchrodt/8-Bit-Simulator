from Code.Intel8080.CycleClasses.Childs.States.acc_to_mem_from_rp import acc_to_mem_from_rp
from Code.Intel8080.CycleClasses.Childs.States.rp_out_status import rp_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Stax_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rp_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(acc_to_mem_from_rp(processor))
