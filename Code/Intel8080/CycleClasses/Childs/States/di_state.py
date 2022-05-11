from Code.Intel8080.CycleClasses.Parents.State import State


class di_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("di_state")
        self.processor.interrupt_enabled = False
        self.processor.StateLogger.addEntry("di_state")
