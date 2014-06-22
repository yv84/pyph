import numpy

from .len_packet import LenL2PacketRcv, LenL2PacketSend
from .xor import Xor
from .gs_l2_packet import gs_l2_packet, PacketError


class KeyInit():
    def __init__(self, packet):
        self.packet = packet
        self.packet.server.command_stack.append(lambda data: self.key_packet_initialization(data))
        self.gameapi = gs_l2_packet()

    def key_packet_initialization(self, to_s_data: bytes) -> bytes:
        def key_packet_initialization_remover(to_s_data):
            self.packet.server.command_stack.pop()  # key_packet_initialization_remover
            self.packet.server.command_stack.pop(0) # key_packet_initialization
            self.packet.client.xor_in = self.packet.client.xor_out = self.packet.server.xor_in
            return to_s_data
        if to_s_data.startswith(b'\x19\x00.'):
            for stack, obj in zip([self.packet.client.command_stack, self.packet.server.command_stack],
                     [self.packet.client, self.packet.server]):
                stack.append(lambda data: obj.pck_rcv.segmentation_packets(data))
                stack.append(lambda gen: obj.xor_in.xor(gen))
                stack.append(lambda gen, manager=self.packet.manager, name=obj.name,
                   peername=self.packet.peername : self.packet.manager.set_manager_data(name, gen, peername))
                stack.append(lambda gen, name=obj.name, gameapi=self.gameapi, peername=self.packet.peername: \
                    self.packet_print_dtype(name, gameapi, gen, peername))
                stack.append(lambda gen: obj.xor_out.xor(gen))
                stack.append(lambda gen: obj.pck_send.add_packets(gen))
                stack.append(lambda gen: obj.pck_send.pop_packet()) # -> bytes(data)
            self.packet.server.command_stack.append(lambda data: key_packet_initialization_remover(data))
        return to_s_data

    def packet_print_dtype(self, name, gameapi, gen, peername):
        for packet in gen:
            print("{}: ".format(name), end='')
            side = 's' if name == 'server' else 'c'
            try:
                unpack = gameapi.unpack(packet, side)
                pack = gameapi.pack(unpack, side)
                if isinstance(unpack, numpy.ndarray):
                    print("{ ", end='')
                    for i, j in zip(unpack.item(), unpack.dtype.fields):
                        print(j, "=", i, end='; ')
                    print("} ")
                yield pack
            except PacketError:
                print('error parsing packet')
                print("{}: ".format(name), end='')
                print(packet)
                yield packet





class Connect():
    def __init__(self, name):
        self.name = name
        self._data = b''
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        self.pck_rcv = LenL2PacketRcv()
        self.pck_send = LenL2PacketSend()
        self.xor_in = Xor('decode')
        self.xor_out = Xor('code')


# stack.append(lambda gen, manager=self.packet.manager, name=obj.name,
#    peername=self.packet.peername : self.packet.manager.set_manager_data(name, gen, peername))
