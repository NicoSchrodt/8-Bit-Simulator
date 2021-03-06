from Code.Intel8080.CycleClasses.Parents.State import State


class ccc_is_true(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("ccc_is_true")

        ccc = self.processor.get_ccc()

        result = False

        if ccc == 0:
            result = not self.processor.ALU.get_zero_flag()
        elif ccc == 1:
            result = self.processor.ALU.get_zero_flag()
        elif ccc == 2:
            result = not self.processor.ALU.get_carry_flag()
        elif ccc == 3:
            result = self.processor.ALU.get_carry_flag()
        elif ccc == 4:
            result = not self.processor.ALU.get_parity_flag()
        elif ccc == 5:
            result = self.processor.ALU.get_parity_flag()
        elif ccc == 6:
            result = not self.processor.ALU.get_sign_flag()
        elif ccc == 7:
            result = self.processor.ALU.get_sign_flag()

        if not result:
            self.processor.skip_rest_of_instruction = True
        self.processor.StateLogger.addEntry("ccc_is_true")
