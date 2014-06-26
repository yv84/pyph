import asyncio
from asyncio.queues import Queue, QueueEmpty


class Packet():

    def __init__(self, manager, peername):
        if manager.cmd_line.game == 'raw':
            from raw.key_init import KeyInit, Connect
        elif manager.cmd_line.game == 'l2':
            from l2.key_init import KeyInit, Connect
        elif manager.cmd_line.game == 'aa':
            from aa.key_init import KeyInit, Connect

        self.client = Connect('client')
        self.client.q = Queue()
        self.server = Connect('server')
        self.server.q = Queue()
        self.manager = manager
        self.peername = peername
        self.key_init = KeyInit(self)

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
            gen = to_data
            for cmd in stack:
                gen = cmd(gen)
            to_data = gen
        for q, data in zip([self.client.q, self.server.q],
                            [to_c_data, to_s_data]):
            if data:
                q.put_nowait(data)
