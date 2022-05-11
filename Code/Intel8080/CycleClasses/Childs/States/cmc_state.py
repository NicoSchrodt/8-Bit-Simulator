from Code.Intel8080.CycleClasses.Parents.State import State


class cmc_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("cmc_state")
        self.processor.ALU.set_carry_flag(self.processor.ALU.get_carry_flag() ^ 1)
        self.processor.StateLogger.addEntry("cmc_state")
