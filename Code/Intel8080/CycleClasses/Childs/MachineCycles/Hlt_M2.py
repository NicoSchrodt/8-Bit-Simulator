from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Childs.States.set_halt_mode import set_halt_mode
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Hlt_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(pc_out_status(processor))
        self.states.append(set_halt_mode(processor))
