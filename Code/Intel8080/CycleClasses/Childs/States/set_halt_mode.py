from Code.Intel8080.CycleClasses.Parents.State import State


class set_halt_mode(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("set_halt_mode")
        self.processor.halt = True
        self.processor.StateLogger.addEntry("set_halt_mode")
