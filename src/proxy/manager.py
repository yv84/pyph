
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
        self.ws_handler = None
        if self.cmd_line.game == 'l2':
            from l2.gs_l2_packet import gs_l2_packet
            self.gameapi = gs_l2_packet()
        elif self.cmd_line.game == 'aa':
            pass
        else:
            raise Exception('invalid cmd_line.game')

    def set_manager_data(self, side, gen, peername):
        if self.ws_handler.websockets:
            for packet in gen:
                self.packets.append([peername, side, repr(packet)[1:]])
                yield packet
        else:
            yield from gen
