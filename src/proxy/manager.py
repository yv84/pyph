class Side():
    def __init__(self):
        self.packets_to_ws = []
        self.packets_to_gs = []

class Manager():
    def __init__(self):
        self.client = Side()
        self.server = Side()
        self.data = ''
        self.packets = []
