from Code.Intel8080.CycleClasses.Childs.States.xor_state import xor_state
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Xor_MC(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(xor_state(processor))
