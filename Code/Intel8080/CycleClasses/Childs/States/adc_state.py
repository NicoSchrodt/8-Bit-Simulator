from Code.Intel8080.CycleClasses.Parents.State import State


class adc_state(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("adc_state")
        act = self.processor.get_act()
        tmp = self.processor.get_tmp()
        cy = self.processor.ALU.get_carry_flag()

        ac, cy, result = self.processor.ALU.binary_add(act, tmp, cy)
        self.processor.ALU.set_cy_ac_flags(cy, ac)
        self.processor.ALU.evaluate_zsp_flags(True, True, True, result)
        # TODO Anmerkung [9] auf Seite 34 vermerken in doku
        self.processor.set_acc(result)