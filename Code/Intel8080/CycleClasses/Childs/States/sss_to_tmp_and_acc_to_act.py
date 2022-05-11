from Code.Intel8080.CycleClasses.Childs.States.SubParents.byte_at_pc_minus_1_ import byte_at_pc_minus_1_


class sss_to_tmp_and_acc_to_act(byte_at_pc_minus_1_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("sss_to_tmp_and_acc_to_act")
        sss = self.byte & self.processor.sss_mask
        rp = self.processor.registers.get_register_with_offset(sss)
        self.processor.set_tmp(rp)

        acc = self.processor.get_acc()
        self.processor.set_act(acc)
        self.processor.StateLogger.addEntry("sss_to_tmp_and_acc_to_act")
