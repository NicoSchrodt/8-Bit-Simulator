from Code.Intel8080.CycleClasses.Childs.States.SubParents.byte_at_pc_minus_1_ import byte_at_pc_minus_1_


class acc_to_mem_from_rp(byte_at_pc_minus_1_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("acc_to_mem_from_rp")
        acc = self.processor.get_acc()
        rp_address = self.processor.get_rp_address()

        if self.processor.get_current_rp() <= 1:
            self.processor.set_memory_byte(rp_address, acc)
