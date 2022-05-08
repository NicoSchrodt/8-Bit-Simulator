from Code.Intel8080.CycleClasses.Childs.States.byte_at_pc_to_w import byte_at_pc_to_w
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Childs.States.pc_incr import pc_incr
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Jmp_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(pc_incr(processor))
        self.states.append(byte_at_pc_to_w(processor))
