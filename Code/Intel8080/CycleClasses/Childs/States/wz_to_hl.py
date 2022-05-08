from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class wz_to_hl(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("wz_to_hl")
        w_val = self.processor.registers.get_register_with_offset(char_to_reg("W"))
        z_val = self.processor.registers.get_register_with_offset(char_to_reg("Z"))

        self.processor.registers.set_register8_with_offset(char_to_reg("H"), w_val)
        self.processor.registers.set_register8_with_offset(char_to_reg("L"), z_val)
