from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class sp_minus_1_to_z(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sp_minus_1_to_z")
        old_sp = self.processor.get_memory_byte(self.processor.get_sp() - 1)
        self.processor.registers.set_register8_with_offset(char_to_reg("Z"), old_sp)
