
from .packet_buffer import Packet


class Side():
    def __init__(self):
        self.packets_to_ws = []
        self.packets_to_gs = []


class Manager():

    def __init__(self, cmd_line, base_dir, *args, **kw):
        self.base_dir = base_dir
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
            from l2.gs_l2_packet import GSL2Packet
            self.gameapi = GSL2Packet()
        else:
            raise Exception('invalid cmd_line.game')

    def create_connection(self, peername):
        self.list_gs_conn_append(peername)
        return Packet(self, peername)

    @property
    def list_gs_conn(self):
        return self._list_gs_conn

    def list_gs_conn_append(self, peername):
        self._list_gs_conn.append(peername)
        self.web_socket.client_list_of_gs_conn_should_be_updated = True
        # if waiting -> peername
        for _ws in self.web_socket.ws.get_from_peername('Waiting'):
            _ws.gs_conn = peername[0]+','+str(peername[1])
            _ws.update_require = True
            for pck in _ws._packets_to_gs:
                pck[0] = peername
        self.web_socket.ws.add_ws_conn_to_set()
        return

    def list_gs_conn_remove(self, peername):
        self._list_gs_conn.remove(peername)
        self.web_socket.client_list_of_gs_conn_should_be_updated = True
        return



    def set_manager_data(self, side, gen, peername):
        if self.web_socket.ws.peernames():
            yield from self.web_socket.ws.get_packets_to_gs(peername[0]+','+str(peername[1]), side)

            if peername[0]+','+str(peername[1]) in self.web_socket.ws.peernames():
                for _packet in gen:
                    for _ws in self.web_socket.ws.get_from_peername(
                                peername[0]+','+str(peername[1])):
                        _ws.packets.append([peername, side, repr(_packet)[1:]])
                    yield _packet
            else:
                yield from gen
        else:
            yield from gen
