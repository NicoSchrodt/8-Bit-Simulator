from Code.Intel8080.CycleClasses.Childs.MachineCycles.acc_to_act_mc import acc_to_act_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.act_minus_tmp_to_acc_mc import act_minus_tmp_to_acc_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.b2_to_tmp import b2_to_tmp
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Sui(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [acc_to_act_mc(processor),
                               b2_to_tmp(processor),
                               act_minus_tmp_to_acc_mc(processor)]
        pass
