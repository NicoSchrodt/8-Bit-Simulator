from Code.Intel8080.CycleClasses.Parents.State import State


class FetchState2(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        self.processor.registers.increment_pc()
        print("PC = PC + 1 (Fetch 2)")
        pass