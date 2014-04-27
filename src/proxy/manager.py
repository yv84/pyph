class Side():
    def __init__(self):
        self.packets = []

class Manager():
    def __init__(self):
        client = Side()
        server = Side()
        self.data = ''
        self.packets = []
