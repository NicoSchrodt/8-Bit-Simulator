from Code.Intel8080.CycleClasses.Parents.State import State


class reset_w_and_instr_to_instruction_register(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("reset_w_and_instr_to_instruction_register")
        self.processor.registers.set_register8_with_offset("W", 0)

        self.processor.cpu_instruction_register = self.processor.get_byte_from_memory_address_at_pc()
        self.processor.StateLogger.addEntry("reset_w_and_instr_to_instruction_register")
