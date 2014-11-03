from importlib import import_module
from abc import ABCMeta, abstractmethod
import types
import asyncio
from asyncio.queues import Queue, QueueEmpty


class Packet():

    def __init__(self, manager, peername):
        key_init = import_module(manager.cmd_line.game+'.packet_pipe')
        self.manager = manager
        self.peername = peername
        # self.key_init = key_init.KeyInit(self)
        self.client = key_init.Connect('client', self)
        self.server = key_init.Connect('server', self)

    def update_data(self, side, data):
        """change in_data buffer"""
        if side == 'f_c':
            self.client._data = b''.join([self.client._data, data])
        elif side == 'f_s':
            self.server._data = b''.join([self.server._data, data])
        else:
            raise Exception('invalid side')

    @asyncio.coroutine
    def packet_handlers(self):
        """pass through a set of commands"""
        from_c_data, from_s_data = self.client._data, self.server._data
        self.client._data, self.server._data = b'', b''
        gen = (lambda gen: (yield gen))

        # c_tx -> self.client._data -> s_rx
        # c_rx <- self.server._data <- s_tx
        data = b''.join(self.client.pipe.run(gen(from_c_data))) # from client
        if data:
            self.server.q.put_nowait(data) # to server

        data = b''.join(self.server.pipe.run(gen(from_s_data))) # from server
        if data:
            self.client.q.put_nowait(data) # to client
