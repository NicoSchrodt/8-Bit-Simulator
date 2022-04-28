from Code.Intel8080.CycleClasses.Childs.States.byte_at_pc_to_z import byte_at_pc_to_z
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState2 import FetchState2
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Jmp_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(FetchState1(processor))
        self.states.append(FetchState2(processor))
        self.states.append(byte_at_pc_to_z(processor))
