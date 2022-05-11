from Code.Intel8080.CycleClasses.Childs.States.nnn_to_z_and_pcl_to_sp import nnn_to_z_and_pcl_to_sp
from Code.Intel8080.CycleClasses.Childs.States.sp_out_status import sp_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Rst_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sp_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(nnn_to_z_and_pcl_to_sp(processor))
