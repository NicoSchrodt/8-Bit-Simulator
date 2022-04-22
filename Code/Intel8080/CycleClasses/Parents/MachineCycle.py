#from Code.Intel8080.Intel8080 import Intel8080


class MachineCycle:
    def __init__(self, processor): #: Intel8080):
        self.processor = processor
        self.states = []
        self.last_executed_state = 0
        pass

    def next_state(self):
        self.states[self.last_executed_state].run()
        self.last_executed_state += 1
        if self.last_executed_state == len(self.states):
            self.last_executed_state = 0
            return True
        return False
