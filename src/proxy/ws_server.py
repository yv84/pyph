#!/usr/bin/env python

import asyncio
import websockets


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

    def __call__(self, websocket, path):
        return self.ws_handler(websocket, path)

    # @app.route('/')
    @asyncio.coroutine
    def index(self, websocket, path):
        while True:
            if self.manager.packets:
                response = repr(websocket)[1:-1] + ' | ' + repr(path) +\
                    repr(self.manager.data) +\
                    repr(b''.join([b'<p><ol><li>',
                        (b'</li><li>'.join(self.manager.packets)),
                        b'</li></ol></p>']))
                self.manager.packets = []
                print("s:> {}".format(response))
                yield from websocket.send(response)
            else:
                pass
            yield from asyncio.sleep(1)


    @asyncio.coroutine
    def ws_handler(self, websocket, path):
        print(path, end=' , ')
        print(websocket)
        if path == ('/'):
            yield from self.index(websocket, path)
        elif path.startswith('/hello'):
            yield from hello(websocket, path)


def websocket_serve(loop, manager):
    ws_handler = WsHandler(manager)
    start_server = yield from websockets.serve(ws_handler, '0.0.0.0', 8765)
