from Code.Intel8080.CycleClasses.Childs.States.acc_to_sp_plus_1 import acc_to_sp_plus_1
from Code.Intel8080.CycleClasses.Childs.States.sp_decr import sp_decr
from Code.Intel8080.CycleClasses.Childs.States.sp_out_status import sp_out_status
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Push_psw_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sp_out_status(processor))
        self.states.append(sp_decr(processor))
        self.states.append(acc_to_sp_plus_1(processor))
