#!/usr/bin/env python

import asyncio
import websockets

@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect('ws://localhost:8765/')
    #name = input("What's your name? ")
    name = "test"
    yield from websocket.send(name)
    print("c:> {}".format(name))
    greeting = yield from websocket.recv()
    print("c:< {}".format(greeting))
    
    websocket = yield from websockets.connect('ws://localhost:8765/hello')
    #name = input("What's your name? ")
    name = "test"
    yield from websocket.send(name)
    print("c:> {}".format(name))
    greeting = yield from websocket.recv()
    print("c:< {}".format(greeting))

def main():
    asyncio.get_event_loop().run_until_complete(hello())

if __name__ == '__main__':
    main()