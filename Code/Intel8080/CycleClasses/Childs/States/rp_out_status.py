from Code.Intel8080.CycleClasses.Parents.State import State


class rp_out_status(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        print("rp_out_status")
