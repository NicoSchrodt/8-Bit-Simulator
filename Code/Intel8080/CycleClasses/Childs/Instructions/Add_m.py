from Code.Intel8080.CycleClasses.Childs.MachineCycles.acc_to_act_mc import acc_to_act_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Add_m_M2 import Add_m_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.act_plus_tmp_to_acc_mc import act_plus_tmp_to_acc_mc
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Add_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [acc_to_act_mc(processor),
                               Add_m_M2(processor),
                               act_plus_tmp_to_acc_mc(processor)]
        pass
