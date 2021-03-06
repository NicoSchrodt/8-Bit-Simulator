from Code.Intel8080.CycleClasses.Parents.State import State


class sp_minus_1_to_rl(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sp_minus_1_to_rp")
        old_sp = self.processor.get_memory_byte(self.processor.get_sp() - 1)

        rp = self.processor.get_current_rp()
        self.processor.registers.set_register8_with_offset(rp * 2 + 1, old_sp)
        self.processor.StateLogger.addEntry("sp_minus_1_to_rp")
