from Code.Intel8080.CycleClasses.Parents.State import State


class alu_to_a_and_cy(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("alu_to_a_and_cy")
        self.processor.set_acc(self.processor.ALU.get_alu())
        self.processor.ALU.set_carry_flag(self.processor.ALU.get_alu_cy())
