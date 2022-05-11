from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.stc_state import stc_state


class Stc_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(stc_state(processor))
