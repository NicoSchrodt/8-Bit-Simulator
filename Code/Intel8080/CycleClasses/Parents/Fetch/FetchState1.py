from Code.Intel8080.CycleClasses.Parents.State import State


class FetchState1(State):
    def __init__(self, processor):
        super().__init__(processor)

    def run(self):
        # PC OUT STATUS
        print("fetch state 1: run")
        pass
