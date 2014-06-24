# based on http://stackoverflow.com/questions/21295068/how-can-i-create-a-relay-server-using-tulip-asyncio-in-python

import asyncio
from asyncio.queues import Queue, QueueEmpty

from .packet_buffer import Packet


class Client(asyncio.Protocol):

    def connection_made(self, transport):
        self.connected = True
        # save the transport
        self.transport = transport

    def data_received(self, data):
        # forward data to the server
        self.server.buffers[self.peername].update_data('client', data)

    def connection_lost(self, *args):
        self.connected = False
        self.transport.close()


class Server(asyncio.Protocol):

    def __init__(self, loop, manager):
        self.loop = loop
        self.manager = manager
        self.clients = {}
        self.buffers = {}
        super(asyncio.Protocol, self).__init__()

    def connection_made(self, transport):
        # save the transport
        self.transport = transport
        print('Server(asyncio.Protocol) connection_made/', repr(self.transport).split('at')[1], ' id= ',id(self))

    def connection_lost(self, exc):
        print('Server(asyncio.Protocol) connection_lost/', repr(self.transport).split('at')[1], ' id= ',id(self))

    def data_received(self, data):
        """receive data from transport socket"""
        # use a task so this is executed async
        print("RCV: ", repr(self.transport).split('at')[1], ' id= ',id(self))
        asyncio.Task(self.rcv_data(data))

    @asyncio.coroutine
    def rcv_data(self, data):
        """handle obtained connection"""
        # get a client by its peername
        peername = self.transport.get_extra_info('peername')
        client = self.clients.get(peername)
        # create a client if peername is not known or the client disconnect
        if client is None or not client.connected:
            protocol, client = yield from create_client(self.loop)
            client.server = self
            client.peername = peername
            client.server_transport = self.transport
            self.clients[peername] = client
            self.manager.list_gs_conn.append(peername)
            self.buffers[peername] = Packet(self.manager, peername)
            asyncio.Task(self.send_data(peername))
            asyncio.Task(self.data_from_packet_buffer_to_queue(peername))
        self.buffers[peername].update_data('server', data)


    @asyncio.coroutine
    def data_from_packet_buffer_to_queue(self, peername):
        """put out data to queue"""
        while self.clients[peername].connected:
            yield from self.buffers[peername].packet_handlers()
            yield from asyncio.sleep(0.02)
        self.manager.list_gs_conn.remove(peername)
        self.transport.close()

    @asyncio.coroutine
    def send_data(self, peername):
        """take data from queue and send to transport socket"""
        while self.clients[peername].connected:
            # Return any available message
            client_data = asyncio.Task(self.buffers[peername].client.q.get())
            server_data = asyncio.Task(self.buffers[peername].server.q.get())
            done, pending = yield from asyncio.wait(
                [client_data, server_data],
                return_when=asyncio.FIRST_COMPLETED)
            for future_data, transport in zip([client_data, server_data],
                    [self.clients[peername].server_transport,
                    self.clients[peername].transport]):
                if future_data in done:
                    transport.write(future_data.result())
                    print("SEND: ", repr(transport).split('at')[1], ' id= ',id(self))
                else:
                    future_data.cancel()


create_client = lambda loop: loop.create_connection(Client, '127.0.0.1', 9999)

@asyncio.coroutine
def init_proxy(loop, manager):
    yield from loop.create_server(lambda : Server(loop, manager), '127.0.0.1', 8888)
