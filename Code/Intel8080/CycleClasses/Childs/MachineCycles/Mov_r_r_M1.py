from Code.Intel8080.CycleClasses.Childs.States.sss_tmp import sss_tmp
from Code.Intel8080.CycleClasses.Childs.States.tmp_ddd import tmp_ddd
from Code.Intel8080.CycleClasses.Parents.Fetch.Fetch import Fetch


class M1Mov_r_r(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sss_tmp(processor))
        self.states.append(tmp_ddd(processor))
