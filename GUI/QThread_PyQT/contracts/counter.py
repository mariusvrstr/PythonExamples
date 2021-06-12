

class Counter():
    name = None
    raw = None

    def __init__(self, name):
        self.name = name
        self.raw = 0

    def set(self, value):
        self.raw = value

    def incriment(self, value = 1):
        self.raw += value

    def get_value(self):
        return self.raw
        

