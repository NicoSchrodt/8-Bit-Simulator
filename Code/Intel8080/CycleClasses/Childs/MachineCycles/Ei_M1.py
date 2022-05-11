from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.ei_state import ei_state


class Ei_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(ei_state(processor))
