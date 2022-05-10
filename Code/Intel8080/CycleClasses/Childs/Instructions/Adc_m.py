from Code.Intel8080.CycleClasses.Childs.MachineCycles.acc_to_act_mc import acc_to_act_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.act_plus_tmp_plus_cy_to_acc_mc import \
    act_plus_tmp_plus_cy_to_acc_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.data_to_tmp_mc import data_to_tmp_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Adc_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [acc_to_act_mc(processor),
                               data_to_tmp_mc(processor),
                               act_plus_tmp_plus_cy_to_acc_mc(processor)]
        pass
