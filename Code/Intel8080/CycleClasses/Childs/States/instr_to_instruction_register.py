from Code.Intel8080.CycleClasses.Parents.State import State


class instr_to_instruction_register(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("instr -> IR (Fetch 3)")
        self.processor.cpu_instruction_register = self.processor.get_byte_from_memory_address_at_pc()
        pass
