from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg, build_16bit_from_8bit


class acc_to_mem(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("acc_to_mem")
        acc = self.processor.get_acc()

        z_val = self.processor.registers.get_register_with_offset(char_to_reg("Z"))
        w_val = self.processor.registers.get_register_with_offset(char_to_reg("W"))

        address = build_16bit_from_8bit(w_val, z_val)

        self.processor.set_memory_byte(address, acc)
        self.processor.StateLogger.addEntry("acc_to_mem")
