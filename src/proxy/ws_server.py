#!/usr/bin/env python

import json
import asyncio
from asyncio.queues import Queue, QueueEmpty


import websockets

from .repr_to_bytes import from_str_to_repr_bytes


@asyncio.coroutine
def hello(websocket, path):
    name = yield from websocket.recv()
    print("s:< {}".format(name))
    greeting = "Hello {}!".format(name)
    print("s:> {}".format(greeting))
    yield from websocket.send(greeting)



class WsHandler():
    def __init__(self, manager):
        self.manager = manager
        self.manager.ws_handler = self
        self.websockets = {}

    def __call__(self, websocket, path):
        return self.ws_handler(websocket, path)

    # @app.route('/')
    @asyncio.coroutine
    def index(self, websocket, path):
        while True:
            recv = yield from websocket.recv()
            if recv:
                d = json.loads(recv)
                for k,v in d.items():
                    if k == 'c':
                        self.manager.client.packets_to_gs.append(from_str_to_repr_bytes(v))
                    elif k == 's':
                        self.manager.server.packets_to_gs.append(from_str_to_repr_bytes(v))

            if self.manager.packets:
                response = json.dumps(tuple(map (lambda x: repr(x)[2:-1], self.manager.packets )))
                self.manager.packets = []
                for _websocket in [_websocket for _websocket in \
                        self.websockets if \
                        self.websockets.get(_websocket)['path'] == path]:
                    yield from _websocket.send(response)
            else:
                pass
            yield from asyncio.sleep(0.5)


    @asyncio.coroutine
    def ws_handler(self, websocket, path):
        self.websockets[websocket].update({'path': path})
        if path == ('/'):
            yield from self.index(websocket, path)

        elif path.startswith('/hello'):
            yield from hello(websocket, path)



class WebSocketServerProtocol(websockets.WebSocketServerProtocol):

    def connection_made(self, transport):
        self.ws_handler.websockets[self] = {}
        super().connection_made(transport)

    @asyncio.coroutine
    def recv(self):
        """
        This coroutine receives the next message.

        It returns a :class:`str` for a text frame and :class:`bytes` for a
        binary frame.

        Non blocking version
        """
        #Return any available message
        try:
            msg = self.messages.get_nowait()
            return msg
        except QueueEmpty:
            pass

    def connection_lost(self, exc):
        print('connection_lost : {}'.format(self))
        self.ws_handler.websockets.pop(self)
        super().connection_lost(exc)


def websocket_serve(loop, manager):
    ws_handler = WsHandler(manager)
    start_server = yield from websockets.serve(ws_handler,
        '0.0.0.0', 8765, klass=WebSocketServerProtocol, )
