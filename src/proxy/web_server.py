#!/usr/bin/env python3.4
 
import asyncio
 
 
@asyncio.coroutine
def init_web_server(app, loop):
    # use a coroutine to use yield from and get the async result of
    # create_server
    import aiohttp.wsgi
    f = yield from loop.create_server(lambda: aiohttp.wsgi.WSGIServerHttpProtocol(app,
            debug=True, readpayload=True), "0.0.0.0", 5000)
    # srv = loop.run_until_complete(f)
    # socks = srv.sockets
    # print("serving on", [x.getsockname() for x in socks])



