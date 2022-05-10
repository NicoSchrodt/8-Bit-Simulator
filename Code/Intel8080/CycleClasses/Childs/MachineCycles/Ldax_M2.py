from Code.Intel8080.CycleClasses.Childs.States.mem_from_rp_to_acc import mem_from_rp_to_acc
from Code.Intel8080.CycleClasses.Childs.States.rp_out_status import rp_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Ldax_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rp_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(mem_from_rp_to_acc(processor))
