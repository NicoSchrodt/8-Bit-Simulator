from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.cma_state import cma_state


class Cma_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(cma_state(processor))
