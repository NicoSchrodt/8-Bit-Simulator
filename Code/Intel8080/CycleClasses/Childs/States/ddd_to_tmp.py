from Code.Intel8080.CycleClasses.Parents.State import State


class ddd_to_tmp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("ddd_to_tmp")
        ddd = self.processor.get_ddd()
        ddd_val = self.processor.registers.get_register_with_offset(ddd)
        self.processor.set_tmp(ddd_val)
