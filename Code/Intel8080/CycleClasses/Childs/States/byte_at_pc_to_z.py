from Code.Intel8080.CycleClasses.Childs.States.byte_at_pc_ import byte_at_pc_
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class byte_at_pc_to_z(byte_at_pc_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("byte_at_pc_to_z")
        self.processor.registers.set_register8_with_offset(char_to_reg("Z"), self.b2)
