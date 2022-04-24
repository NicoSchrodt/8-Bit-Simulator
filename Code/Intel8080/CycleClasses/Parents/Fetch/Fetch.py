from Code.Intel8080.CycleClasses.Parents.EmtpyState import EmptyState
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState2 import FetchState2
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState3 import FetchState3
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Fetch(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states = [FetchState1(processor), FetchState2(processor), FetchState3(processor),
                       ]
