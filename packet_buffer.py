from l2.len_packet import LenL2PacketRcv, LenL2PacketSend


class Buffer():
    def __init__(self):
        self._data = {'client': b'', 'server': b''} # from side
        self.client_pck_rcv = LenL2PacketRcv()
        self.server_pck_rcv = LenL2PacketRcv()
        self.client_pck_send = LenL2PacketSend()
        self.server_pck_send = LenL2PacketSend()

    def update_data(self, side, data):
        if side == 'client':
            self._data['client'] = b''.join([self._data['client'], data])
        elif side == 'server':
            self._data['server'] = b''.join([self._data['server'], data])
        else:
            raise Exception('invalid side')

    def run(self):
        to_c_data, to_s_data = self._data['client'], self._data['server']
        self._data['client'], self._data['server'] = b'', b''

        self.client_pck_rcv.add_packet(to_s_data)
        [self.client_pck_send.add_packet(i) for i in self.client_pck_rcv.pop_packets()]
        to_s_data = self.client_pck_send.pop_packet()

        self.server_pck_rcv.add_packet(to_c_data)
        [self.server_pck_send.add_packet(i) for i in self.server_pck_rcv.pop_packets()]
        to_c_data = self.server_pck_send.pop_packet()


        return to_c_data, to_s_data # to side
