from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.swap_hl_with_de import swap_hl_with_de


class Xchg_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(swap_hl_with_de(processor))
