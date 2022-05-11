from Code.Intel8080.CycleClasses.Parents.State import State


class rh_to_act(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("rh_to_act")
        rp = self.processor.get_current_rp()

        if self.processor.rp_means_sp():
            sp_high = self.processor.get_sp() & 0xff00
            self.processor.set_act(sp_high)
        else:
            high, low = self.processor.get_rp_values(rp)
            self.processor.set_act(high)
        self.processor.StateLogger.addEntry("rh_to_act")
