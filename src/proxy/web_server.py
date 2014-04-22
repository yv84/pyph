# https://www.gitorious.org/aiohttp-werkzeug-demo/aiohttp-werkzeug-demo/source/a8fbc257805d927281bf75ea338d6dae321df2b2:demo.py#L60 
import asyncio

import aiohttp.wsgi 
 

@asyncio.coroutine
def init_web_server(app, loop):
    # use a coroutine to use yield from and get the async result of
    # create_server
    f = yield from loop.create_server(lambda: aiohttp.wsgi.WSGIServerHttpProtocol(app,
            debug=True, readpayload=True), "0.0.0.0", 5000)
    # srv = loop.run_until_complete(f)
    # socks = srv.sockets
    # print("serving on", [x.getsockname() for x in socks])



