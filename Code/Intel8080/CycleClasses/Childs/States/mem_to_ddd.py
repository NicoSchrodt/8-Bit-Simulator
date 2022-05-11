from Code.Intel8080.CycleClasses.Parents.State import State


class mem_to_ddd(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("mem_to_ddd")
        mem_val = self.processor.get_memory_byte()
        self.processor.StateLogger.addEntry("mem_to_ddd")
