from l2.len_packet import LenL2PacketRcv, LenL2PacketSend


class Connect():
    def __init__(self):
        self._data = b''
        self.pck_rcv = LenL2PacketRcv()
        self.pck_send = LenL2PacketSend()
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        self.command_stack.append(lambda gen: self.pck_send.add_packets(gen()))


class Packet():
    def __init__(self):
        self._data = {'client': b'', 'server': b''} # from side
        self.client = Connect()
        self.server = Connect()

    def update_data(self, side, data):
        if side == 'client':
            self.client._data = b''.join([self.client._data, data])
        elif side == 'server':
            self.server._data = b''.join([self.server._data, data])
        else:
            raise Exception('invalid side')

    def run(self):
        to_c_data, to_s_data = self.client._data, self.server._data
        self.client._data, self.server._data = b'', b''

        self.client.pck_rcv.add_packet(to_s_data)
        print(self.client.pck_rcv.get_packets())
        gen = self.client.pck_rcv.pop_packets
        for cmd in self.client.command_stack:
            gen = cmd(gen)
        to_s_data = self.client.pck_send.pop_packet()

        self.server.pck_rcv.add_packet(to_c_data)
        gen = self.server.pck_rcv.pop_packets
        for cmd in self.server.command_stack:
            gen = cmd(gen)
        to_c_data = self.server.pck_send.pop_packet()

        return to_c_data, to_s_data # to side


        #[self.client_pck_send.add_packet(i) for i in self.client_pck_rcv.pop_packets()]
        # xor(code/decode): [some_pck_logic.add(decode(i)) for i in self.client_pck_rcv.pop_packets()]
        # time logic: some_pck_logic.time_logic_add()
        # xor(code/decode): [self.client_pck_send.add_packet(code(i)) for i in self.some_pck_logic.pop_packets()]
        # some_logic(x: generator) -> generator