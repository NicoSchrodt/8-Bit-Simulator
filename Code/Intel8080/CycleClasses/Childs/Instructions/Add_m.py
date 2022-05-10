from Code.Intel8080.CycleClasses.Childs.MachineCycles.acc_to_act_mc import acc_to_act_mc
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Add_m_M2 import Add_m_M2
from Code.Intel8080.CycleClasses.Childs.MachineCycles.Add_MC import Add_MC
from Code.Intel8080.CycleClasses.Parents.Instruction import Instruction


class Add_m(Instruction):
    def __init__(self, processor):
        super().__init__(processor)
        self.machine_cycles = [acc_to_act_mc(processor),
                               Add_m_M2(processor),
                               Add_MC(processor)]
        pass
