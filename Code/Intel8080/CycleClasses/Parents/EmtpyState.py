from Code.Intel8080.CycleClasses.Parents.State import State


class EmptyState(State):
    def __init__(self, processor=None):
        super().__init__(processor)


