from Code.Intel8080.CycleClasses.Childs.States.rh_to_sp_plus_1 import rh_to_sp_plus_1
from Code.Intel8080.CycleClasses.Childs.States.sp_decr import sp_decr
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Push_rp_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(sp_decr(processor))
        self.states.append(rh_to_sp_plus_1(processor))
