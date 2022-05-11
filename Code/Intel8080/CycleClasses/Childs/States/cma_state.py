from Code.Intel8080.CycleClasses.Parents.State import State


class cma_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("cma_state")
        acc = self.processor.get_acc() ^ 0xFF
        self.processor.set_acc(acc)
        self.processor.StateLogger.addEntry("cma_state")
