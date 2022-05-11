from Code.Intel8080.CycleClasses.Parents.State import State


class tmp_to_data(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("tmp_to_data")
        self.processor.set_memory_byte(self.processor.get_h_l_address(), self.processor.get_tmp())
        self.processor.StateLogger.addEntry("tmp_to_data")
