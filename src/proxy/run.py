import sys

assert sys.version >= '3.3', 'Please use Python 3.3 or higher.'
import asyncio

from .proxy import init_proxy
from .web_server import init_web_server


def run():
    loop = asyncio.get_event_loop()
    server = None

    # main task to initialize everything
    task1 = asyncio.Task(init_proxy(loop))
    task2 = asyncio.Task(init_web_server(loop))
    # run
    try:
        server = loop.run_forever()
    except KeyboardInterrupt:
        print("exit")
    except:
        print("killed")
    finally:
        task1.close()
        task2.close()
        loop.close()

if __name__ == '__main__':
    run()