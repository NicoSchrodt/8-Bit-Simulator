from Code.Intel8080.CycleClasses.Childs.States.SubParents.byte_at_pc_ import byte_at_pc_


class byte_at_pc_to_rl(byte_at_pc_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("byte_at_pc_to_rl")
        rp = self.processor.get_current_rp()

        if self.processor.rp_means_sp():
            self.processor.set_sp_l(self.byte)
        else:
            self.processor.registers.set_register8_with_offset(rp * 2 + 1, self.byte)
        self.processor.StateLogger.addEntry("byte_at_pc_to_rl")
