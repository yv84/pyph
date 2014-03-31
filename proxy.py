# based on http://stackoverflow.com/questions/21295068/how-can-i-create-a-relay-server-using-tulip-asyncio-in-python
import asyncio

from packet_buffer import Buffer

class Client(asyncio.Protocol):

    def connection_made(self, transport):
        self.connected = True
        # save the transport
        self.transport = transport

    def data_received(self, data):
        # forward data to the server
        self.server.buffers[self.peername].update_data('client', data)
        print('S: ', data)

    def connection_lost(self, *args):
        self.connected = False


class Server(asyncio.Protocol):
    clients = {}
    buffers = {}
    def connection_made(self, transport):
        # save the transport
        self.transport = transport

    @asyncio.coroutine
    def send_data(self, data):
        # get a client by its peername
        peername = self.transport.get_extra_info('peername')
        client = self.clients.get(peername)
        # create a client if peername is not known or the client disconnect
        if client is None or not client.connected:
            protocol, client = yield from loop.create_connection(
                Client, '127.0.0.1', 9999)
            client.server = self
            client.peername = peername
            client.server_transport = self.transport
            self.clients[peername] = client
            self.buffers[peername] = Buffer()
            asyncio.Task(self.run(peername))
        self.buffers[peername].update_data('server', data)

    @asyncio.coroutine
    def run(self, peername):
        while self.clients[peername].connected:
            client_data, server_data = self.buffers[peername].run()
            if client_data:
                self.clients[peername].server_transport.write(client_data)
            if server_data:
                self.clients[peername].transport.write(server_data)
            yield from asyncio.sleep(0.1)

    def data_received(self, data):
        # use a task so this is executed async
        print('C: ', data)
        asyncio.Task(self.send_data(data))

@asyncio.coroutine
def initialize(loop):
    # use a coroutine to use yield from and get the async result of
    # create_server
    server = yield from loop.create_server(Server, '127.0.0.1', 8888)

loop = asyncio.get_event_loop()
server = None

# main task to initialize everything
asyncio.Task(initialize(loop))

# run
try:
    loop.run_forever()
except KeyboardInterrupt:
    print("exit")
finally:
    server.close()
    loop.close()

