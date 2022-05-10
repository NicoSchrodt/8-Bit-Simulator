from Code.Intel8080.CycleClasses.Childs.States.l_to_wz_minus_1 import l_to_wz_minus_1
from Code.Intel8080.CycleClasses.Childs.States.wz_incr import wz_incr
from Code.Intel8080.CycleClasses.Childs.States.wz_out_status import wz_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Shld_M4(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(wz_out_status(processor))
        self.states.append(wz_incr(processor))
        self.states.append(l_to_wz_minus_1(processor))
