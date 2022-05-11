from Code.Intel8080.CycleClasses.Parents.State import State


class rl_to_act(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("rl_to_act")
        rp = self.processor.get_current_rp()

        if self.processor.rp_means_sp():
            sp_low = self.processor.get_sp() & 0x00ff
            self.processor.set_act(sp_low)
        else:
            high, low = self.processor.get_rp_values(rp)
            self.processor.set_act(low)
