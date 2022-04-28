from Code.Intel8080.CycleClasses.Parents.State import State


class sss_to_tmp(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("sss_to_tmp")
        self.processor.set_tmp(self.processor.get_sss_value())
