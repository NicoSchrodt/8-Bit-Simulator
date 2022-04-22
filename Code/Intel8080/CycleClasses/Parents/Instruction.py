#from Code.Intel8080.Intel8080 import Intel8080


class Instruction:

    def __init__(self, processor): #: Intel8080):
        self.machine_cycles = []
        self.last_executed_machine_cycle = 0
        pass

    def next_state(self):
        if self.machine_cycles[self.last_executed_machine_cycle].next_state():
            self.last_executed_machine_cycle += 1

        if self.last_executed_machine_cycle == len(self.machine_cycles):
            self.last_executed_machine_cycle = 0
            return True
        return False

    def next_machine_cycle(self):
        while not self.machine_cycles[self.last_executed_machine_cycle].next_state():
            pass

        self.last_executed_machine_cycle += 1
        return self.last_executed_machine_cycle == len(self.machine_cycles)

    def execute_complete_instruction(self):
        while not self.next_state():
            pass

    def load_m1_t4(self):
        self.machine_cycles[0].last_executed_state = 3
