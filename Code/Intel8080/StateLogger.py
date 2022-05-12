class StateLogger:
    def __init__(self, TextWidget):
        self.Widget = TextWidget

    def clearLog(self):
        self.Widget.clear()

    def addEntry(self, string):
        self.Widget.appendPlainText(string)


class DummyLogger:
    def __init__(self):
        pass

    def clearLog(self):
        pass

    def addEntry(self, string):
        pass
