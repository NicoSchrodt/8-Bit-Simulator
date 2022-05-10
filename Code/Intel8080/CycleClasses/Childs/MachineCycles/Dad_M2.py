from Code.Intel8080.CycleClasses.Childs.States.act_plus_tmp_to_l import act_plus_tmp_to_l
from Code.Intel8080.CycleClasses.Childs.States.l_to_tmp import l_to_tmp
from Code.Intel8080.CycleClasses.Childs.States.rl_to_act import rl_to_act
from Code.Intel8080.CycleClasses.Parents.MachineCycle import MachineCycle


class Dad_M2(MachineCycle):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(rl_to_act(processor))
        self.states.append(l_to_tmp(processor))
        self.states.append(act_plus_tmp_to_l(processor))
