import itertools

from asyncio.queues import Queue, QueueEmpty
from proxy.packet_buffer import Pipe


class Connect():
    def __init__(self, name, packet):
        self.name = name
        self.packet = packet
        self._data = b''
        self.q = Queue()
        self.pipe = PacketPipe(self)


class PacketPipe(Pipe):
    def __init__(self, connect):
        self.connect = connect
        self.packet = self.connect.packet
        if self.connect.name == 'server': # s -> c
            self.pck_func = [self.initialization, ]
        else: # c -> s
            self.pck_func = [self.initialization, ]

    def run(self, pck_gen):
        func = self.pck_func[:]
        for f in func:
            pck_gen = f(pck_gen)
        return pck_gen

    def initialization(self, pck_gen):
        self.packet.server.pipe.pck_func = [
                self.remove_empty_packets,
                self.packet.server.pipe.pck_manager,
            ]
        self.packet.client.pipe.pck_func = [
                self.remove_empty_packets,
                self.packet.client.pipe.pck_manager,
            ]
        yield from pck_gen

    def remove_empty_packets(self, pck_gen):
        for packet in pck_gen:
            if packet:
                yield packet

    def pck_manager(self, pck_gen):
        yield from self.packet.manager.set_manager_data(
            self.connect.name, pck_gen, self.packet.peername)