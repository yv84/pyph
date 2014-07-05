from .len_packet import LenPackets

class KeyInit():
    def __init__(self, packet):
        self.packet = packet
        self.packet.client.command_stack.append(lambda data: self.key_packet_initialization(data))

    def key_packet_initialization(self, to_c_data: bytes) -> bytes:
        def key_packet_initialization_remover(to_c_data):
            self.packet.client.command_stack.pop()  # key_packet_initialization_remover
            self.packet.client.command_stack.pop(0) # key_packet_initialization
            return to_c_data
        if to_c_data:
            for stack, obj in zip([self.packet.client.command_stack, self.packet.server.command_stack],
                     [self.packet.client, self.packet.server]):
                stack.append(lambda data: obj.pck_len.pck_in(data))
                # stack.append(lambda gen, name=obj.name: packet_print(name, gen))
                stack.append(lambda gen, manager=self.packet.manager, name=obj.name,
                   peername=self.packet.peername : self.packet.manager.set_manager_data(name, gen, peername))
                stack.append(lambda gen: obj.pck_len.pck_out(gen))
            self.packet.client.command_stack.append(lambda data: key_packet_initialization_remover(data))
        return to_c_data


class Connect():
    def __init__(self, name):
        self.name = name
        self._data = b''
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        self.pck_len = LenPackets()


def packet_print(name, gen):
    for packet in gen:
        print(packet)
        yield packet
