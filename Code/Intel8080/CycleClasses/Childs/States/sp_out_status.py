from Code.Intel8080.CycleClasses.Parents.State import State


class sp_out_status(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sp_out_status")
        self.processor.StateLogger.addEntry("sp_out_status")
