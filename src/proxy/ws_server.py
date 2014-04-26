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
def  index(websocket, path):
    response = '<h1>Index page</h1><a href="/async">async</a>, <a href="/demo">async-demo</a>, <a href="/flask">flask</a>'
#       '<p>' + repr(loop) + '</p>' + '<p>' + repr(app) + '</p>' + \
#       '<p>' + repr(manager.data) + '</p>' +\
#       repr(b''.join([b'<p><ol><li>',
#           (b'</li><li>'.join(manager.packets)),
#           b'</li></ol></p>']))
    print("s:> {}".format(response))
    yield from websocket.send(response)

@asyncio.coroutine
def site(websocket, path):
    print(path, end=' , ')
    print(websocket)
    if path == ('/'):
        yield from index(websocket, path)
    elif path.startswith('/hello'):
        yield from hello(websocket, path)


def websocket_serve(loop):
    start_server = yield from websockets.serve(site, 'localhost', 8765)

