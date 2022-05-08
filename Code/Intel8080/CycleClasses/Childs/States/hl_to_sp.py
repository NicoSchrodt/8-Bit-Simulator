from Code.Intel8080.CycleClasses.Parents.State import State


class hl_to_sp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("hl_to_sp")
        self.processor.set_sp(self.processor.get_h_l_address())