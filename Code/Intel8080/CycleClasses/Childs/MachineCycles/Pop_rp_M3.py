from Code.Intel8080.CycleClasses.Childs.States.sp_incr import sp_incr
from Code.Intel8080.CycleClasses.Childs.States.sp_minus_1_to_rh import sp_minus_1_to_rh
from Code.Intel8080.CycleClasses.Childs.States.sp_out_status import sp_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Pop_rp_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sp_out_status(processor))
        self.states.append(sp_incr(processor))
        self.states.append(sp_minus_1_to_rh(processor))
