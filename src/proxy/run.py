import sys

assert sys.version >= '3.3', 'Please use Python 3.3 or higher.'
import asyncio

from flask import Flask

from .proxy import init_proxy
from .web_server import init_web_server
from .urls import flask_route

from .manager import Manager


def run():
    loop = asyncio.get_event_loop()
    server = None

    # main task to initialize everything
    manager = Manager()
    
    task1 = asyncio.Task(init_proxy(loop, manager))
    
    flask_app = flask_route(loop, manager)
    task2 = asyncio.Task(init_web_server(flask_app, loop))

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