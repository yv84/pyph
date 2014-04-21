import sys

assert sys.version >= '3.3', 'Please use Python 3.3 or higher.'
import asyncio

from proxy import init_proxy
from web_server import init_web_server

loop = asyncio.get_event_loop()
server = None

# main task to initialize everything
asyncio.Task(init_proxy(loop))
asyncio.Task(init_web_server(loop))

# run
try:
    loop.run_forever()
except KeyboardInterrupt:
    print("exit")
except:
	print("killed")
finally:
    server.close()
    loop.close()