from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.hl_to_sp import hl_to_sp
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState


class Sphl_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(hl_to_sp(processor))
