from Code.Intel8080.CycleClasses.Childs.States.alu_to_a_and_cy import alu_to_a_and_cy
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class alu_to_a_and_cy_mc(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(alu_to_a_and_cy(processor))
