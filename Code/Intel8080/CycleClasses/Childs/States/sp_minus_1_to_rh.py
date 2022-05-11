from Code.Intel8080.CycleClasses.Parents.State import State


class sp_minus_1_to_rh(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sp_minus_1_to_rh")
        old_sp = self.processor.get_memory_byte(self.processor.get_sp() - 1)

        rp = self.processor.get_current_rp()
        self.processor.registers.set_register8_with_offset(rp * 2, old_sp)
