from Code.Intel8080.CycleClasses.Childs.States.wz_out_status import wz_out_status
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class In_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(wz_out_status(processor))
        self.states.append(EmptyState(processor))
        self.states.append(EmptyState(processor))   # Should write external data to acc,
                                                    # no intend to communicate with external
