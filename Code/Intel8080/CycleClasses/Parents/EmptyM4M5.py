from Code.Intel8080.CycleClasses.Childs.MachineCycles.Fetch import Fetch
from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState


class EmptyM4M5(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(EmptyState(processor))
        self.states.append(EmptyState(processor))
