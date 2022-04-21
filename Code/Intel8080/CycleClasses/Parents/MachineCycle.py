class MachineCycle:
    def __init__(self, processor):
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
