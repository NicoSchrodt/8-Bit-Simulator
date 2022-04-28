from Code.Intel8080.CycleClasses.Parents.State import State


class mem_ddd(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("mem_ddd")
        mem_val = self.processor.get_memory_byte()
