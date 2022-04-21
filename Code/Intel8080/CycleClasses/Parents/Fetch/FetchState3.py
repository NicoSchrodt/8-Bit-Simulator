from Code.Intel8080.CycleClasses.Parents.State import State


class FetchState3(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        # instr-> TMP/IR
        print("fetch state 3: run")
        pass
