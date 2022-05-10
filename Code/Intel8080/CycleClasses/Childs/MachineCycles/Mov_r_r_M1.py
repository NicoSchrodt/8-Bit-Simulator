from Code.Intel8080.CycleClasses.Childs.States.sss_to_tmp import sss_to_tmp
from Code.Intel8080.CycleClasses.Childs.States.tmp_to_ddd import tmp_to_ddd
from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch


class Mov_r_r_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sss_to_tmp(processor))
        self.states.append(tmp_to_ddd(processor))
