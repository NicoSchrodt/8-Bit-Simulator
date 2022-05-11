from Code.Intel8080.CycleClasses.Parents.State import State


class hl_to_pc(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("hl_to_pc")
        self.processor.set_pc(self.processor.get_h_l_address())
        self.processor.StateLogger.addEntry("hl_to_pc")
