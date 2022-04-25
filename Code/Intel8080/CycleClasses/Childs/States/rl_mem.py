from Code.Intel8080.CycleClasses.Parents.State import State


class rl_mem(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("rl_mem")
        high, low = self.processor.get_rp_values((self.processor.cpu_instruction_register & 0x30) >> 4)
        self.processor.set_memory_byte(self.processor.get_sp() + 1, low)
