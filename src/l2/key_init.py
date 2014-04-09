from .len_packet import LenL2PacketRcv, LenL2PacketSend
from .xor import Xor
from .gs_l2_packet import gs_l2_packet


class KeyInit():
    def __init__(self, packet):
        self.server = packet.server
        self.client = packet.client
        self.server.command_stack.append(lambda data: self.key_packet_initialization(data))
        self.gameapi = gs_l2_packet()


    def key_packet_initialization(self, to_s_data: bytes) -> bytes:
        def key_packet_initialization_remover(to_s_data):
            self.server.command_stack.pop()  # key_packet_initialization_remover
            self.server.command_stack.pop(0) # key_packet_initialization
            self.client.xor_in = self.client.xor_out = self.server.xor_in
            return to_s_data

        if to_s_data.startswith(b'\x19\x00.'):
            for stack, obj in zip([self.client.command_stack, self.server.command_stack],
                     [self.client, self.server]):
                stack.append(lambda data: obj.pck_rcv.segmentation_packets(data))
                # stack.append(lambda gen: obj.xor_in.xor(gen))
                #(lambda name : stack.append(lambda gen: packet_print(name, gen)))(obj.name)
                (lambda name, gameapi : stack.append(lambda gen: \
                    packet_print_dtype(name, gameapi, gen)))(obj.name, self.gameapi)
                # stack.append(lambda gen: obj.xor_out.xor(gen))
                stack.append(lambda gen: obj.pck_send.add_packets(gen))
                stack.append(lambda gen: obj.pck_send.pop_packet()) # -> bytes(data)
            self.server.command_stack.append(lambda data: key_packet_initialization_remover(data))
        return to_s_data


class Connect():
    def __init__(self, name):
        self.name = name
        self._data = b''
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        self.pck_rcv = LenL2PacketRcv()
        self.pck_send = LenL2PacketSend()
        self.xor_in = Xor('decode')
        self.xor_out = Xor('code')


def packet_print(name, gen):
    for packet in gen:
        print("{}: ".format(name), end='')
        print(packet)
        yield packet

def packet_print_dtype(name, gameapi, gen):
    for packet in gen:
        print("{}: ".format(name), end='')
        side = 's' if name == 'server' else 'c'
        try:
            unpack = gameapi.unpack(packet, side)
            pack = gameapi.pack(unpack, side)
            print(pack)
            yield pack
        except:
            print('error parsing packet')
            #print(packet)
            yield packet