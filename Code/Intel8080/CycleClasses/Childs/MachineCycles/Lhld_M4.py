from Code.Intel8080.CycleClasses.Childs.States.wz_minus_1_to_l import wz_minus_1_to_l
from Code.Intel8080.CycleClasses.Childs.States.wz_incr import wz_incr
from Code.Intel8080.CycleClasses.Childs.States.wz_out_status import wz_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Lhld_M4(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(wz_out_status(processor))
        self.states.append(wz_incr(processor))
        self.states.append(wz_minus_1_to_l(processor))
