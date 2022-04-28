from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Childs.States.pc_incr import pc_incr
from Code.Intel8080.CycleClasses.Childs.States.instr_to_instruction_register import instr_to_instruction_register
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Fetch(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [pc_out_status(processor), pc_incr(processor), instr_to_instruction_register(processor),
                       ]
