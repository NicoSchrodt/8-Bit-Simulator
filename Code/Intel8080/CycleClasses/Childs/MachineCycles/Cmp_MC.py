from Code.Intel8080.CycleClasses.Childs.States.cmp_state import cmp_state
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Cmp_MC(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(cmp_state(processor))
