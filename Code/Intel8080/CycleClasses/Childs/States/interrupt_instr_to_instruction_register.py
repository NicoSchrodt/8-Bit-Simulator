from Code.Intel8080.CycleClasses.Parents.State import State


class interrupt_instr_to_instruction_register(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("interrupt_instr_to_instruction_register")
        self.processor.StateLogger.addEntry("interrupt_instr_to_instruction_register")

        self.processor.cpu_instruction_register = self.processor.interrupt_instruction
