from Code.Intel8080.CycleClasses.Childs.MachineCycles.SubParents.Fetch import Fetch
from Code.Intel8080.CycleClasses.Childs.States.acc_to_act import acc_to_act


class acc_to_act_mc(Fetch):
    def __init__(self, processor):
        super().__init__(processor)
        self.states.append(acc_to_act(processor))
