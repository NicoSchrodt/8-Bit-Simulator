from Code.Intel8080.CycleClasses.Childs.States.data_to_tmp import data_to_tmp
from Code.Intel8080.CycleClasses.Childs.States.hl_out_status import hl_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class data_to_tmp_mc(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(hl_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(data_to_tmp(processor))
