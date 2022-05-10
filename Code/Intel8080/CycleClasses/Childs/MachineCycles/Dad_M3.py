from Code.Intel8080.CycleClasses.Childs.States.act_plus_tmp_plus_cy_to_h import act_plus_tmp_plus_cy_to_h
from Code.Intel8080.CycleClasses.Childs.States.h_to_tmp import h_to_tmp
from Code.Intel8080.CycleClasses.Childs.States.rh_to_act import rh_to_act
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Dad_M3(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rh_to_act(processor))
        self.states.append(h_to_tmp(processor))
        self.states.append(act_plus_tmp_plus_cy_to_h(processor))
