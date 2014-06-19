#!/usr/bin/env python

import asyncio
import websockets

@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect('ws://localhost:8765/hello')
    #name = input("What's your name? ")
    name = "test"
    yield from websocket.send(name)
    #print("c:> {}".format(name))
    greeting = yield from websocket.recv()
    #print("c:< {}".format(greeting))


@asyncio.coroutine
def index():
    websocket = yield from websockets.connect('ws://localhost:8765/')
    while True:
        name = "test"
        yield from websocket.send(name)
        #print("c:> {}".format(name))
        greeting = yield from websocket.recv()
        #print("c:< {}".format(greeting))
        yield from asyncio.sleep(4)

@asyncio.coroutine
def index1():
    pass

def main():
    pass
    #asyncio.get_event_loop().run_until_complete(index())

if __name__ == '__main__':
    main()