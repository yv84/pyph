import asyncio

from flask import Flask, render_template
#from flask_sockets import Sockets as WebSocket


def flask_route(loop, manager):
    app = Flask(__name__)
    #sockets = WebSocket(app)
    app.debug = True

    @app.route('/')
    def index():
        return render_template('websocket.html')
        # response = '<h1>Index page</h1><a href="/async">async</a>, <a href="/demo">async-demo</a>, <a href="/flask">flask</a>' + \
        #   '<p>' + repr(loop) + '</p>' + '<p>' + repr(app) + '</p>' + \
        #   '<p>' + repr(manager.data) + '</p>' +\
        #   repr(b''.join([b'<p><ol><li>',
        #       (b'</li><li>'.join(manager.packets)),
        #       b'</li></ol></p>']))



    return app

