from Code.Intel8080.CycleClasses.Childs.States.act_AND_tmp_to_acc import act_AND_tmp_to_acc
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class act_AND_tmp_to_acc_mc(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(act_AND_tmp_to_acc(processor))
