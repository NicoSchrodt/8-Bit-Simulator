from Code.Intel8080.CycleClasses.Childs.States.interrupt_instr_to_instruction_register import \
    interrupt_instr_to_instruction_register
from Code.Intel8080.CycleClasses.Childs.States.interrupt_t1 import interrupt_t1
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Interrupt_M1(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [interrupt_t1(processor),
                       EmptyState(processor),
                       interrupt_instr_to_instruction_register(processor),
                       EmptyState(processor)]  # last state added, so decode instruction (in T4) will be called
