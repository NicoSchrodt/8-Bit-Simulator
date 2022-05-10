from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.sss_to_tmp_and_acc_to_act import sss_to_tmp_and_acc_to_act


class sss_to_tmp_and_acc_to_act_mc(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(sss_to_tmp_and_acc_to_act(processor))
