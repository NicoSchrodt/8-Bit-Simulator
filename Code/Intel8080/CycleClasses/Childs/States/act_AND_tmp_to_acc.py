from Code.Intel8080.CycleClasses.Parents.State import State


class act_AND_tmp_to_acc(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("act_AND_tmp_to_acc")
        result = self.processor.get_act() & self.processor.get_tmp()
        self.processor.set_acc(result)

        self.processor.ALU.set_carry_flag(False)