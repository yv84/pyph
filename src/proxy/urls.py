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


    return app

