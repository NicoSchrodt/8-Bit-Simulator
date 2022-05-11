from Code.Intel8080.CycleClasses.Parents.State import State
from Code.Intel8080.Intel8080_Components.Intel8080_ALU import char_to_reg


class act_plus_tmp_to_l(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("act_plus_tmp_to_l")
        act = self.processor.get_act()
        tmp = self.processor.get_tmp()

        ac, cy, result = self.processor.ALU.binary_add(act, tmp, 0)
        self.processor.ALU.set_carry_flag(cy)
        self.processor.registers.set_register8_with_offset(char_to_reg("L"), result)
        self.processor.StateLogger.addEntry("act_plus_tmp_to_l")
