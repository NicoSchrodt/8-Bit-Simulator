from Code.Intel8080.CycleClasses.Parents.State import State


class tmp_ddd(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("tmp_ddd")
        self.processor.set_ddd(self.processor.get_tmp())
