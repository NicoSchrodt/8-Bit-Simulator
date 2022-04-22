from Code.Intel8080.CycleClasses.Parents.Fetch.Fetch import Fetch
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class FetchInstruction(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [Fetch(processor)]
