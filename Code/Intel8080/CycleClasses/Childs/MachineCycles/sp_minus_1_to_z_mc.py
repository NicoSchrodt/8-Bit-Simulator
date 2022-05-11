from Code.Intel8080.CycleClasses.Childs.States.sp_incr import sp_incr
from Code.Intel8080.CycleClasses.Childs.States.sp_minus_1_to_z import sp_minus_1_to_z
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class sp_minus_1_to_z_mc(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(sp_incr(processor))
        self.states.append(sp_minus_1_to_z(processor))
