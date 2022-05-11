from Code.Intel8080.CycleClasses.Parents.State import State


class stc_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("stc_state")
        self.processor.ALU.set_carry_flag(True)
