from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.Fetch import Fetch


class M2Mov(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [EmptyState(), EmptyState()]

