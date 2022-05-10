from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.ddd_to_tmp import ddd_to_tmp
from Code.Intel8080.CycleClasses.Childs.States.tmp_plus_one_to_ddd import tmp_plus_one_to_ddd


class Inr_r_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(ddd_to_tmp(processor))
        self.states.append(tmp_plus_one_to_ddd(processor))
