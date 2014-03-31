#from l2.len_packet import LenL2PacketRcv, LenL2PacketSend


class Buffer():
    def __init__(self):
        self._data = {'client': b'', 'server': b''}

    def update_data(self, side, data):
        if side == 'client':
            self._data['client'] = b''.join([self._data['client'], data])
        elif side == 'server':
            self._data['server'] = b''.join([self._data['server'], data])
        else:
            raise Exception('invalid side')

    def run(self):
        c_data, s_data = self._data['client'], self._data['server']
        self._data['client'], self._data['server'] = b'', b''
        return c_data, s_data
