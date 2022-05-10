from Code.Intel8080.CycleClasses.Childs.States.or_state import or_state
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Or_MC(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(or_state(processor))

