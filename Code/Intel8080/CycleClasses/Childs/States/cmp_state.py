from Code.Intel8080.CycleClasses.Parents.State import State


class cmp_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("cmp_state")
        act = self.processor.get_act()
        tmp = self.processor.get_tmp()
        result = act - 0 - tmp  # -0 to get rid of 8 bit range

        self.processor.ALU.set_zero_flag(result == 0)
        self.processor.ALU.set_carry_flag(result < 0)
