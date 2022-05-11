from Code.Intel8080.CycleClasses.Parents.State import State


class acc_to_act(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("acc_to_act")
        acc = self.processor.get_acc()
        self.processor.set_act(acc)
        self.processor.StateLogger.addEntry("acc_to_act")
