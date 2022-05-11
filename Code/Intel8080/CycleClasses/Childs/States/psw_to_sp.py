from Code.Intel8080.CycleClasses.Parents.State import State


class psw_to_sp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("psw_to_sp")
        psw = self.processor.get_processor_status_word()
        self.processor.set_memory_byte(self.processor.get_sp(), psw)
