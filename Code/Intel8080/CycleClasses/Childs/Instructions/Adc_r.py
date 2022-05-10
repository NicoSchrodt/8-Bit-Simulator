from Code.Intel8080.CycleClasses.Childs.MachineCycles.act_plus_tmp_plus_cy_to_acc_mc import \
    act_plus_tmp_plus_cy_to_acc_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.sss_to_tmp_and_acc_to_act_mc import sss_to_tmp_and_acc_to_act_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Adc_r(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [sss_to_tmp_and_acc_to_act_mc(processor),
                               act_plus_tmp_plus_cy_to_acc_mc(processor)]
        pass
