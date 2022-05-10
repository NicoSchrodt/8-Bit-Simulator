from Code.Intel8080.CycleClasses.Childs.States.SubParents.byte_at_pc_ import byte_at_pc_


class byte_at_pc_to_rh(byte_at_pc_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("byte_at_pc_to_rh")
        rp = self.processor.get_current_rp() * 2 + 1
        self.processor.registers.set_register8_with_offset(rp, self.byte)
