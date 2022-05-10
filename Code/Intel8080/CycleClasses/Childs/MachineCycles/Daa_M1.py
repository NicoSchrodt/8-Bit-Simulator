from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.daa_state import daa_state


class Daa_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(daa_state(processor))
