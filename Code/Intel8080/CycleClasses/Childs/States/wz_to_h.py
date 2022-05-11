from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class wz_to_h(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("wz_to_h")
        wz = self.processor.get_wz()

        wz_val = self.processor.get_memory_byte(wz)
        self.processor.registers.set_register8_with_offset(char_to_reg("H"), wz_val)
        self.processor.StateLogger.addEntry("wz_to_h")
