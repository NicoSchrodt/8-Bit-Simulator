from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.rlc_state import rlc_state


class Rlc_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rlc_state(processor))
