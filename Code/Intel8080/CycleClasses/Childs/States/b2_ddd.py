from Code.Intel8080.CycleClasses.Parents.State import State

# byte 2 to ddd
class b2_ddd(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("b2_ddd")
        self.processor.set_ddd(self.processor.get_byte_from_memory_at_pc())
