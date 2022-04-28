from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Pc_incr import Pc_incr
from Code.Intel8080.CycleClasses.Childs.States.byte_at_pc_to_rh import byte_at_pc_to_rh


class Lxi_M3(Pc_incr):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(byte_at_pc_to_rh(processor))
