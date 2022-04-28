from Code.Intel8080.CycleClasses.Childs.States.byte_at_pc_to_ddd import byte_at_pc_to_ddd
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Childs.States.pc_incr import pc_incr


class Mvi_r_M2(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [pc_out_status(processor), pc_incr(processor), byte_at_pc_to_ddd(processor)]
