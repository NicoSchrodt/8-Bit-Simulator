from Code.Intel8080.CycleClasses.Childs.States.sub_state import sub_state
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Sub_MC(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(sub_state(processor))
