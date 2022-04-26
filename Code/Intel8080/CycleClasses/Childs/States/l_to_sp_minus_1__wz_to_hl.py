from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class l_to_sp_minus_1__wz_to_hl(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("l_to_sp_minus_1__wz_to_hl")
        l_val = self.processor.registers.get_register_with_offset(char_to_reg("L"))
        self.processor.set_memory_byte(self.processor.get_sp() - 1, l_val)

        w_val = self.processor.registers.get_register_with_offset(char_to_reg("W"))
        z_val = self.processor.registers.get_register_with_offset(char_to_reg("Z"))

        self.processor.registers.set_register8_with_offset(char_to_reg("H"), w_val)
        self.processor.registers.set_register8_with_offset(char_to_reg("L"), z_val)
