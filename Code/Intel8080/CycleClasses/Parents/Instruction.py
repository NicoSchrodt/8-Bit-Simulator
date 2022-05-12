#from Code.Intel8080.Intel8080 import Intel8080


class Instruction:

    def __init__(self, processor): #: Intel8080):
        self.machine_cycles = []
        self.last_executed_machine_cycle = 0
        pass

    # returns True if last state of last machine cycle was executed
    def next_state(self):
        if self.machine_cycles[self.last_executed_machine_cycle].next_state():
            self.last_executed_machine_cycle += 1
            return True
        return False

    def load_m1_t4(self):
        self.machine_cycles[0].last_executed_state = 3

    def get_machine_cycles(self):
        return self.machine_cycles
