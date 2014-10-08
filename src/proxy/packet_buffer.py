from importlib import import_module
from abc import ABCMeta, abstractmethod
import types
import asyncio
from asyncio.queues import Queue, QueueEmpty


class Connect():
    def __init__(self, name, packet):
        from l2.len_packet import LenPackets
        from l2.xor import XorInOut
        self.name = name
        self._data = b''
        self.q = Queue()
        self.command_stack = [] # func(gen: types.GeneratorType) -> types.GeneratorType
        self.pck_len = LenPackets()
        self.xor = XorInOut(packet)



class Packet():

    def __init__(self, manager, peername):
        key_init = import_module(manager.cmd_line.game+'.key_init')
        self.client = Connect('client', self)
        self.server = Connect('server', self)
        self.manager = manager
        self.peername = peername
        self.key_init = key_init.KeyInit(self)

    def update_data(self, side, data):
        """change in_data buffer"""
        if side == 'client':
            self.client._data = b''.join([self.client._data, data])
        elif side == 'server':
            self.server._data = b''.join([self.server._data, data])
        else:
            raise Exception('invalid side')

    @asyncio.coroutine
    def packet_handlers(self):
        """pass through a set of commands"""
        to_c_data, to_s_data = self.client._data, self.server._data
        self.client._data, self.server._data = b'', b''
        for stack, to_data in zip([self.client.command_stack,
                                  self.server.command_stack],
                                  [to_s_data, to_c_data]):
            gen = (lambda gen: (yield gen))(to_data)
            for cmd in stack:
                gen = cmd(gen)
            to_data = b''.join(gen)
        for q, data in zip([self.client.q, self.server.q],
                            [to_c_data, to_s_data]):
            if data:
                q.put_nowait(data)
