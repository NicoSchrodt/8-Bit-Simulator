from Code.Intel8080.CycleClasses.Childs.States.byte_at_pc_to_ddd import byte_at_pc_to_ddd
from Code.Intel8080.CycleClasses.Parents.Fetch.Fetch import Fetch
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState2 import FetchState2


class M2Mvi_r(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [FetchState1(processor), FetchState2(processor), byte_at_pc_to_ddd(processor)]
