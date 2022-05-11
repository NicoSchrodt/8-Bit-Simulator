from Code.Intel8080.CycleClasses.Parents.State import State


class ei_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("ei_state")
        self.processor.interrupt_enabled = True
        self.processor.StateLogger.addEntry("ei_state")
