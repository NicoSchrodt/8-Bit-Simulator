from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.rrc_state import rrc_state


class Rrc_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rrc_state(processor))
