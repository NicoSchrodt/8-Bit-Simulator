#from Code.Intel8080.Intel8080 import Intel8080


class State:
    def __init__(self, processor): #: Intel8080):
        self.processor = processor
        pass

    def run(self):
        print("default state: run")
        pass
