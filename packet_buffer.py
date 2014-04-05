from l2.len_packet import LenL2PacketRcv, LenL2PacketSend
from l2.xor import Xor



class Connect():
    def __init__(self):
        self._data = b''
        self.pck_rcv = LenL2PacketRcv()
        self.pck_send = LenL2PacketSend()
        self.xor_in = Xor('decode')
        self.xor_out = Xor('code')
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        

class Packet():
    def __init__(self):
        self._data = {'client': b'', 'server': b''} # from side
        self.client = Connect()
        self.server = Connect()
        self.server.command_stack.append(lambda data: self.key_packet_initialization(data))

    def key_packet_initialization(self, to_s_data: bytes) -> bytes:
        def key_packet_initialization_remover(data):
            self.server.command_stack.pop()  # key_packet_initialization_remover
            self.server.command_stack.pop(0) # key_packet_initialization
            return data

        if to_s_data.startswith(b'\x19\x00.'):
            for stack, obj in zip([self.client.command_stack, self.server.command_stack],
                     [self.client, self.server]):
                stack.append(lambda data: obj.pck_rcv.segmentation_packets(data))
                stack.append(lambda gen: obj.xor_in.xor(gen))
                stack.append(lambda gen: obj.xor_out.xor(gen))
                stack.append(lambda gen: obj.pck_send.add_packets(gen))
                stack.append(lambda gen: obj.pck_send.pop_packet())
            self.server.command_stack.append(lambda gen: key_packet_initialization_remover(gen))
            # self.client.xor_in = self.xor_in
        return to_s_data




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

        for stack, to_data in zip([self.client.command_stack, self.server.command_stack],
                    [to_s_data, to_c_data]):
            gen = to_data
            for cmd in stack:
                gen = cmd(gen)
            to_data = gen

        print(to_c_data, to_s_data)
        return to_c_data, to_s_data # to side
