import json
import asyncio
from asyncio.queues import Queue, QueueEmpty

import websockets

from .repr_to_bytes import from_str_to_repr_bytes


class WsHandler():
    def __init__(self, manager):
        self.manager = manager
        self.manager.ws_handler = self
        self.websockets = {}

    def __call__(self, websocket, path):
        return self.ws_handler(websocket, path)


    def send_to_subscribers(self, path):
        return [_websocket for _websocket in \
                self.websockets if \
                self.websockets.get(_websocket)['path'] == path]

    # @app.route('/')
    @asyncio.coroutine
    def index(self, websocket, path):
        gs_conn = -1
        response = json.dumps({'conn':self.manager.list_gs_conn})
        print('self.manager.list_gs_conn:', response)
        for _ws in self.send_to_subscribers(path):
            yield from _ws.send(response)
        while True:
            recv = yield from websocket.recv()
            if recv:
                d = json.loads(recv)
                for k,v in d.items():
                    if k == 'c':
                        self.manager.client.packets_to_gs.append(from_str_to_repr_bytes(v))
                        print('c: ', v)
                    elif k == 's':
                        self.manager.server.packets_to_gs.append(from_str_to_repr_bytes(v))
                        print('s: ', v)
                    elif k == 'conn':
                        #gs_conn = int(k['conn'])
                        print('gs_conn: ', v.split(','))
                        print(self.manager.list_gs_conn)

            if self.manager.packets:
                response = json.dumps(self.manager.packets)
                self.manager.packets = []
                for _ws in self.send_to_subscribers(path):
                    yield from _ws.send(response)
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
