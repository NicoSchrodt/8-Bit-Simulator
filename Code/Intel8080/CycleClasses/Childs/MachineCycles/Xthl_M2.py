from Code.Intel8080.CycleClasses.Childs.States.sp_minus_1_to_z import sp_minus_1_to_z
from Code.Intel8080.CycleClasses.Childs.States.sp_plus_1 import sp_plus_1
from Code.Intel8080.CycleClasses.Parents.Fetch.FetchState1 import FetchState1
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Xthl_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(FetchState1(processor))
        self.states.append(sp_plus_1(processor))
        self.states.append(sp_minus_1_to_z(processor))
