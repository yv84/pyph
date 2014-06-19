import numpy

from .len_packet import LenL2PacketRcv, LenL2PacketSend


class KeyInit():
    def __init__(self, packet):
        self.server = packet.server
        self.client = packet.client
        self.manager = packet.manager
        self.client.command_stack.append(lambda data: self.key_packet_initialization(data))
        #self.gameapi = gs_l2_packet()


    def key_packet_initialization(self, to_c_data: bytes) -> bytes:
        def key_packet_initialization_remover(to_c_data):
            self.client.command_stack.pop()  # key_packet_initialization_remover
            self.client.command_stack.pop(0) # key_packet_initialization
            return to_c_data
        if to_c_data:
            for stack, obj in zip([self.client.command_stack, self.server.command_stack],
                     [self.client, self.server]):
                stack.append(lambda data: obj.pck_rcv.segmentation_packets(data))
                (lambda name, manager : stack.append(lambda gen: set_manager_data(name, manager, gen)))(obj.name, self.manager)
                (lambda name : stack.append(lambda gen: packet_print(name, gen)))(obj.name)
                # if packet[1:2] in (b'\x03', b'\x04'): inflate(packet) -> deflate(packet)
                # (lambda name, gameapi : stack.append(lambda gen: \
                #     packet_print_dtype(name, gameapi, gen)))(obj.name, self.gameapi)
                stack.append(lambda gen: obj.pck_send.add_packets(gen))
                stack.append(lambda gen: obj.pck_send.pop_packet()) # -> bytes(data)
            self.client.command_stack.append(lambda data: key_packet_initialization_remover(data))
        return to_c_data


class Connect():
    def __init__(self, name):
        self.name = name
        self._data = b''
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        self.pck_rcv = LenL2PacketRcv()
        self.pck_send = LenL2PacketSend()


def set_manager_data(name, manager, gen):
    while manager.client.packets_to_gs:
        yield manager.client.packets_to_gs.pop()
    while manager.server.packets_to_gs:
        yield manager.server.packets_to_gs.pop()
    for packet in gen:
        manager.packets.append(b''.join([name.encode('latin-1'), b': ', packet]))
        yield packet

def packet_print(name, gen):

    for packet in gen:
        if packet[1:2] == b'\x05': # нужны примеры пакетов \x03 \x04
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