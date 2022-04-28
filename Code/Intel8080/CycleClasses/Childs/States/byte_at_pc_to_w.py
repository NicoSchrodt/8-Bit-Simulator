from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class byte_at_pc_to_w(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("byte_at_pc_to_w")
        mem_val = self.processor.get_byte_from_memory_at_pc_minus_1()
        self.processor.registers.set_register8_with_offset(char_to_reg("W"), mem_val)
