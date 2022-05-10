from Code.Intel8080.CycleClasses.Childs.States.SubParents.byte_at_pc_minus_1_ import byte_at_pc_minus_1_


class mem_from_rp_to_acc(byte_at_pc_minus_1_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("mem_from_rp_to_acc")
        rp_address = self.processor.get_rp_address()

        if self.processor.get_current_rp() <= 1:
            self.processor.set_acc(self.processor.get_memory_byte(rp_address))
