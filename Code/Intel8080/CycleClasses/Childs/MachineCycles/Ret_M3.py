from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Childs.States.sp_incr import sp_incr
from Code.Intel8080.CycleClasses.Childs.States.sp_to_w import sp_to_w
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Ret_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(sp_incr(processor))
        self.states.append(sp_to_w(processor))
