
class Side():
    def __init__(self):
        self.packets_to_ws = []
        self.packets_to_gs = []


class Manager():

    def __init__(self, cmd_line, *args, **kw):
        self.client = Side()
        self.server = Side()
        self.data = ''
        self.packets = []
        self.cmd_line = cmd_line
        self.list_gs_conn = []


    def set_manager_data(self, name, gen, peername):
        while self.client.packets_to_gs:
            print(self.client.packets_to_gs)
            yield self.client.packets_to_gs.pop()
        while self.server.packets_to_gs:
            print(self.server.packets_to_gs)
            yield self.server.packets_to_gs.pop()
        for packet in gen:
            self.packets.append([peername, name, repr(packet)[1:]])
            yield packet
