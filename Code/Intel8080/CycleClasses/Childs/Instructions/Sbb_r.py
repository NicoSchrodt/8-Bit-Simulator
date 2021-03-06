from Code.Intel8080.CycleClasses.Childs.MachineCycles.Sbb_MC import \
    Sbb_MC
from Code.Intel8080.CycleClasses.Childs.MachineCycles.sss_to_tmp_and_acc_to_act_mc import sss_to_tmp_and_acc_to_act_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Sbb_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [sss_to_tmp_and_acc_to_act_mc(processor),
                               Sbb_MC(processor)]
        pass
