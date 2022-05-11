from Code.Intel8080.CycleClasses.Childs.States.pc_incr import pc_incr
from Code.Intel8080.CycleClasses.Childs.States.pc_out_status import pc_out_status
from Code.Intel8080.CycleClasses.Childs.States.reset_w_and_instr_to_instruction_register import \
    reset_w_and_instr_to_instruction_register
from Code.Intel8080.CycleClasses.Childs.States.sp_decr import sp_decr
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Rst_M1(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [pc_out_status(processor),
                       pc_incr(processor),
                       reset_w_and_instr_to_instruction_register(processor),
                       EmptyState(processor),
                       sp_decr(processor)]
