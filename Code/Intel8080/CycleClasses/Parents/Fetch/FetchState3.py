from Code.Intel8080.CycleClasses.Parents.State import State


class FetchState3(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("instr -> IR (Fetch 3)")
        self.processor.cpu_instruction_register = self.processor.get_byte_from_memory_at_pc()
        pass
