from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.rar_state import rar_state


class Rar_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rar_state(processor))
