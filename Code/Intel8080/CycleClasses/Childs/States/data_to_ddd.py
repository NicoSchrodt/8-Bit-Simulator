from Code.Intel8080.CycleClasses.Childs.States.data_to_ import data_to_


class data_to_ddd(data_to_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("data_to_ddd")
        self.processor.set_ddd(self.data)
