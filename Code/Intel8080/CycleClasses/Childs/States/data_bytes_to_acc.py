from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg, build_16bit_from_8bit


class data_bytes_to_acc(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("data_bytes_to_acc")
        z_val = self.processor.registers.get_register_with_offset(char_to_reg("Z"))
        w_val = self.processor.registers.get_register_with_offset(char_to_reg("W"))

        address = build_16bit_from_8bit(w_val, z_val)
        value = self.processor.get_memory_byte(address)
        self.processor.set_acc(value)
        self.processor.StateLogger.addEntry("data_bytes_to_acc")
