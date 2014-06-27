
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
        self._list_gs_conn = []
        self.web_socket = None
        if self.cmd_line.game in ('aa', 'raw'):
            pass
        elif self.cmd_line.game == 'l2':
            from l2.gs_l2_packet import gs_l2_packet
            self.gameapi = gs_l2_packet()
        else:
            raise Exception('invalid cmd_line.game')

    @property
    def list_gs_conn(self):
        return self._list_gs_conn

    def list_gs_conn_append(self, peername):
        self._list_gs_conn.append(peername)
        self.web_socket.client_list_of_gs_conn_should_be_updated = True
        return

    def list_gs_conn_remove(self, peername):
        self._list_gs_conn.remove(peername)
        self.web_socket.client_list_of_gs_conn_should_be_updated = True
        return



    def set_manager_data(self, side, gen, peername):
        if self.web_socket.ws.peernames():
            while self.client.packets_to_gs:
                print(self.client.packets_to_gs)
                yield self.client.packets_to_gs.pop()
            while self.server.packets_to_gs:
                print(self.server.packets_to_gs)
                yield self.server.packets_to_gs.pop()
            if peername[0]+','+str(peername[1]) in self.web_socket.ws.peernames():
                for packet in gen:
                    for _ws in self.web_socket.ws.get_ws():
                        if _ws.gs_conn == peername[0]+','+str(peername[1]):
                            _ws.packets.append([peername, side, repr(packet)[1:]])
                    yield packet
            else:
                yield from gen
        else:
            yield from gen
