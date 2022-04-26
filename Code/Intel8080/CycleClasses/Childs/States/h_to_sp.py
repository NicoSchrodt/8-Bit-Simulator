from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class h_to_sp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("h_to_sp")
        h_val = self.processor.registers.get_register_with_offset(char_to_reg("H"))
        self.processor.set_memory_byte(self.processor.get_sp(), h_val)
