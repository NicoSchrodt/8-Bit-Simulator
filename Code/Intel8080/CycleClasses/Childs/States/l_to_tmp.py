from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class l_to_tmp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("l_to_tmp")
        l_val = self.processor.registers.get_register_with_offset(char_to_reg("L"))
        self.processor.set_tmp(l_val)
