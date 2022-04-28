from Code.Intel8080.CycleClasses.Childs.States.rl_to_sp import rl_to_sp
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Push_rp_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(rl_to_sp(processor))
