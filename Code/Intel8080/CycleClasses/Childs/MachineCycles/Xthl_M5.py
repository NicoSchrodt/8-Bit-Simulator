from Code.Intel8080.CycleClasses.Childs.States.l_to_sp_minus_1 import l_to_sp_minus_1
from Code.Intel8080.CycleClasses.Childs.States.wz_to_hl import wz_to_hl
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Xthl_M5(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(l_to_sp_minus_1(processor))
        self.states.append(EmptyState(processor))
        self.states.append(wz_to_hl(processor))
