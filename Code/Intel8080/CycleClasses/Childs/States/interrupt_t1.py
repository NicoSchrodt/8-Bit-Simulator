from Code.Intel8080.CycleClasses.Parents.State import State


class interrupt_t1(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("interrupt_t1")
        self.processor.StateLogger.addEntry("interrupt_t1")
