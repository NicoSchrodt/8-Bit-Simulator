from Code.Intel8080.CycleClasses.Childs.States.SubParents.data_to_ import data_to_


class data_to_tmp(data_to_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("data_to_tmp")
        self.processor.set_tmp(self.data)
        self.processor.StateLogger.addEntry("data_to_tmp")
