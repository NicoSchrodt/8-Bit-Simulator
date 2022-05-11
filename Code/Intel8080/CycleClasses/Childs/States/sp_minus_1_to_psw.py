from Code.Intel8080.CycleClasses.Parents.State import State


class sp_minus_1_to_psw(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sp_minus_1_to_psw")
        old_sp = self.processor.get_memory_byte(self.processor.get_sp() - 1)

        self.processor.set_processor_status_word(old_sp)
        self.processor.StateLogger.addEntry("sp_minus_1_to_psw")
