from Code.Intel8080.CycleClasses.Childs.MachineCycles.sss_to_tmp_and_acc_to_act_mc import sss_to_tmp_and_acc_to_act_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Add_MC import Add_MC
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Add_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [sss_to_tmp_and_acc_to_act_mc(processor),
                               Add_MC(processor)]
        pass
