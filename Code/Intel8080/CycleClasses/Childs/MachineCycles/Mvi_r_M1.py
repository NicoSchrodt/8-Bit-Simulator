from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.Fetch import Fetch


class M1Mvi_r(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(EmptyState(processor))

