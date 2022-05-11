from Code.Intel8080.CycleClasses.Childs.States.wz_out_status import wz_out_status
from Code.Intel8080.CycleClasses.Childs.States.wz_plus_1_to_pc import wz_plus_1_to_pc
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class wz_plus_1_to_pc_mc(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(wz_out_status(processor))
        self.states.append(wz_plus_1_to_pc(processor))
