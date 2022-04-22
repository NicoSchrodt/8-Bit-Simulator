from Code.Intel8080.CycleClasses.Childs.States.sss_tmp import sss_tmp
from Code.Intel8080.CycleClasses.Childs.States.tmp_ddd import tmp_ddd
from Code.Intel8080.CycleClasses.Parents.Fetch.Fetch import Fetch
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState2 import FetchState2
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState3 import FetchState3


class M1Mov_r_r(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [FetchState1(processor), FetchState2(processor), FetchState3(processor),
                       sss_tmp(processor), tmp_ddd(processor)]
