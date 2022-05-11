from Code.Intel8080.CycleClasses.Parents.State import State


class tmp_to_ddd(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("tmp_to_ddd")
        self.processor.set_ddd(self.processor.get_tmp())
        self.processor.StateLogger.addEntry("tmp_to_ddd")
