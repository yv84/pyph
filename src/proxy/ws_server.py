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


# @app.route('/')
@asyncio.coroutine
def index(websocket, path):
    while True:
        response = repr(websocket)[1:-1] + ' | ' + repr(path)
        print("s:> {}".format(response))
        yield from websocket.send(response)
        yield from asyncio.sleep(1)


@asyncio.coroutine
def ws_handler(websocket, path):
    print(path, end=' , ')
    print(websocket)
    if path == ('/'):
        yield from index(websocket, path)
    elif path.startswith('/hello'):
        yield from hello(websocket, path)


def websocket_serve(loop):
    start_server = yield from websockets.serve(ws_handler, '0.0.0.0', 8765)
