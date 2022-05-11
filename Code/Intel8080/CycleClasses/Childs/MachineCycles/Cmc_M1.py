from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.cmc_state import cmc_state


class Cmc_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(cmc_state(processor))
