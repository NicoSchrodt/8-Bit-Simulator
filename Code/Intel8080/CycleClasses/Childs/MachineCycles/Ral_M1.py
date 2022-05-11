from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.ral_state import ral_state
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState


class Ral_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(ral_state(processor))
