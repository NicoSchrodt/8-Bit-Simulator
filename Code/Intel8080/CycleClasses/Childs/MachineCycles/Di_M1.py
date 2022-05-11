from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.di_state import di_state


class Di_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(di_state(processor))
