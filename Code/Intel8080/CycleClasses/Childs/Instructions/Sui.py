from Code.Intel8080.CycleClasses.Childs.MachineCycles.acc_to_act_mc import acc_to_act_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Sub_MC import Sub_MC
from Code.Intel8080.CycleClasses.Childs.MachineCycles.b2_to_tmp import b2_to_tmp
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Sui(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [acc_to_act_mc(processor),
                               b2_to_tmp(processor),
                               Sub_MC(processor)]
        pass
