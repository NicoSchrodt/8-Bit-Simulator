from Code.Intel8080.CycleClasses.Childs.States.sss_to_tmp import sss_to_tmp
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Fetch import Fetch


class Mov_m_r_M1(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sss_to_tmp(processor))
