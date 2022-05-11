from Code.Intel8080.CycleClasses.Parents.State import State


class xor_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("xor_state")
        result = self.processor.get_act() ^ self.processor.get_tmp()
        self.processor.set_acc(result)

        self.processor.ALU.set_cy_ac_flags(False, False)
        self.processor.ALU.evaluate_zsp_flags(True, True, True, result)
