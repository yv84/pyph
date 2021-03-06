#!/usr/bin/env python3
"""TCP echo server example."""
import argparse
import asyncio
import sys
import os
try:
    import signal
except ImportError:
    signal = None


from msg_log import Message
from game_log import log




ARGS = argparse.ArgumentParser(description="PyPh test fixtures.")
ARGS.add_argument(
    '--server', action="store_true", dest='server',
    default=False, help='Run tcp server')
ARGS.add_argument(
    '--client', action="store_true", dest='client',
    default=False, help='Run tcp client')
ARGS.add_argument(
    '--host', action="store", dest='host',
    default='127.0.0.1', help='Host name')
ARGS.add_argument(
    '--port', action="store", dest='port',
    default=9999, type=int, help='Port number')
ARGS.add_argument(
    '--iocp', action="store_true", dest='iocp',
    default=False, help='Use IOCP event loop')

ARGS.add_argument("--game", dest='game', type=str, required=False,
                   help='aa || l2', default='aa')
ARGS.add_argument("--l2_chronicle", dest='l2_chronicle', type=str, required=False,
                   help='so many options', default='gracia_final')

args = ARGS.parse_args()


# ---------------------------------------
if args.game == '_l2':
    f = os.path.join(os.path.dirname(__file__), 'fixtures/l2', 'game_log_with_xor_len.log')
    pattern = {'c': b'client:', 's': b'server:', 'start': 10, 'end': -2}
if args.game == 'l2':
    f = os.path.join(os.path.dirname(__file__), 'fixtures/l2', 'game_log_15122012_with_pck_len.log')
    pattern = {'c': b'client:', 's': b'server:', 'start': 10, 'end': -2}
elif args.game == 'aa':
    f = os.path.join(os.path.dirname(__file__), 'fixtures/aa', 'game_1.log')
    pattern = {'c': b"c->", 's': b"s->", 'start': 3, 'end': -2}
# ---------------------------------------
log = Message.get_log_from_file(f, pattern)
log, side_log = Message.game_log_from_import(log)
print(log, side_log)


class EchoServer(asyncio.Protocol):

    TIMEOUT = 5.0
    message_server = {}

    def timeout(self):
        print('connection timeout, closing.')
        self.transport.close()

    def connection_made(self, transport):
        print('connection made')
        self.transport = transport
        self.message_server[self.transport] = Message('server', log=log, side_log=side_log)

        # start 5 seconds timeout timer
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.TIMEOUT, self.timeout)

    def data_received(self, data):
        #print('data received: ', data.decode())
        #print('S: ', data)
        #self.transport.write(b'Re: ' + data)
        data = b''.join(self.message_server[self.transport](data))
        if data:
            self.transport.write(data)
        else:
            self.transport.close()
        #print('S send: ', b''.join(self.message_server[self.transport](data)))
        # restart timeout timer
        self.h_timeout.cancel()
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.TIMEOUT, self.timeout)

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        print('connection lost:', exc)
        self.h_timeout.cancel()


class EchoClient(asyncio.Protocol):

    message = 'This is the message. It will be echoed.'
    message_client = Message('client', log=log, side_log=side_log)

    def connection_made(self, transport):
        self.transport = transport
        #print(b''.join(self.message_client(b'')))
        self.transport.write(b''.join(self.message_client(b'')))
        #self.transport.write(self.message.encode())
        #print('data sent:', self.message)

    def data_received(self, data):
        #print('C:', data)
        data = b''.join(self.message_client(data))
        if data:
            self.transport.write(data)
        else:
            self.transport.close()
        # disconnect after 10 seconds
        asyncio.get_event_loop().call_later(10.0, self.transport.close)

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        print('connection lost:', exc)
        asyncio.get_event_loop().stop()


def start_client(loop, host, port):
    t = asyncio.Task(loop.create_connection(EchoClient, host, port))
    loop.run_until_complete(t)


def start_server(loop, host, port):
    f = loop.create_server(EchoServer, host, port)
    return loop.run_until_complete(f)


if __name__ == '__main__':

    if ':' in args.host:
        args.host, port = args.host.split(':', 1)
        args.port = int(port)

    if (not (args.server or args.client)) or (args.server and args.client):
        print('Please specify --server or --client\n')
        ARGS.print_help()
    else:
        if args.iocp:
            from asyncio import windows_events
            loop = windows_events.ProactorEventLoop()
            asyncio.set_event_loop(loop)
        else:
            loop = asyncio.get_event_loop()
        print ('Using backend: {0}'.format(loop.__class__.__name__))

        if signal is not None and sys.platform != 'win32':
            loop.add_signal_handler(signal.SIGINT, loop.stop)

        if args.server:
            server = start_server(loop, args.host, args.port)
        else:
            start_client(loop, args.host, args.port)

        try:
            loop.run_forever()
        finally:
            if args.server:
                server.close()
            loop.close()
