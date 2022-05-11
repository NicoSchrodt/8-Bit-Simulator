from Code.Intel8080.CycleClasses.Parents.State import State


class acc_to_sp_plus_1(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("acc_to_sp_plus_1")
        acc = self.processor.get_acc()
        self.processor.set_memory_byte(self.processor.get_sp() + 1, acc)
