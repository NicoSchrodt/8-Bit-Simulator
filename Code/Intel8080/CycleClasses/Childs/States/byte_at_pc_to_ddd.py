from Code.Intel8080.CycleClasses.Childs.States.SubParents.byte_at_pc_ import byte_at_pc_


class byte_at_pc_to_ddd(byte_at_pc_):
    def __init__(self, processor):
        super().__init__(processor)

    def write_to(self):
        print("byte_at_pc_to_ddd")
        self.processor.set_ddd(self.byte)
        self.processor.StateLogger.addEntry("byte_at_pc_to_ddd")
