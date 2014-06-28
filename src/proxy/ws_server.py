import json
import asyncio
from asyncio.queues import Queue, QueueEmpty

import websockets

from .repr_to_bytes import from_str_to_repr_bytes


class Websocket():
    _id_ws = []
    _peernames = set()

    def __init__(self, server_protocol):
        self.server_protocol = server_protocol
        self.path = ''
        self.gs_conn = ''
        self.packets = []
        self.update_require = False
        self._packets_to_gs = []

    def __repr__(self):
        return "<{path} | <p at {server_protocol} | {gs_conn} | <ws at {id}>".format(
            path=self.path, server_protocol=repr(self.server_protocol).split('at')[1],
            gs_conn=self.gs_conn, id=id(self))

    @classmethod
    def send_to_subscribers(cls, path) -> list:
        return [_ws for _ws in cls.get_ws() if _ws.path == path]

    @classmethod
    def get_from_protocol(cls, server_protocol):
        return [_ws for _ws in cls.get_ws() \
           if _ws.server_protocol == server_protocol][0]

    @classmethod
    def get_from_peername(cls, gs_conn) -> list :
        return [_ws for _ws in cls.get_ws() \
           if _ws.gs_conn == gs_conn]

    @classmethod
    def get_from_update_require(cls) -> list :
        return [_ws for _ws in cls.get_ws() \
           if _ws.update_require == True]


    @classmethod
    def add_ws_conn_to_set(cls):
        cls._peernames = set()
        for _ws in cls.get_ws():
            cls._peernames.add(_ws.gs_conn)
        for _ws in cls.get_ws():
            if not _ws.gs_conn in cls._peernames:
                _ws.packets = []  # remove data from buffer if noone needs it

    @classmethod
    def append_ws(cls, obj):
        cls._id_ws.append(obj)

    @classmethod
    def remove_ws(cls, obj):
        cls._id_ws.remove(cls.get_from_protocol(obj))

    @classmethod
    def get_ws(cls):
        return cls._id_ws

    @classmethod
    def peernames(cls):
        return cls._peernames

    @classmethod
    def get_packets_to_gs(cls, peername, side):
        return [] # Not Implemented[peername, side, repr(packet)[1:]]

    def add_packets_to_gs(self, side, pck):
        pass # Not Implemented[peername, side, repr(packet)[1:]]


class WsHandler():
    def __init__(self, manager):
        self.manager = manager
        self.manager.web_socket = self
        self.ws = Websocket
        self.client_list_of_gs_conn_should_be_updated = False

    def __call__(self, websocket, path):
        return self.ws_handler(websocket, path)

    # @app.route('/')
    @asyncio.coroutine
    def index(self, websocket, path):
        self.ws.get_from_protocol(websocket).packets = []
        self.client_list_of_gs_conn_should_be_updated = True

        while True:
            recv = yield from websocket.recv()
            if recv:
                d = json.loads(recv)
                for k,v in d.items():
                    if k == 'c':
                        self.ws.get_from_protocol(websocket).add_packets_to_gs(
                            'client', from_str_to_repr_bytes(v))
                        print('c: ', v)
                    elif k == 's':
                        self.ws.get_from_protocol(websocket).add_packets_to_gs(
                            'server', from_str_to_repr_bytes(v))
                        print('s: ', v)
                    elif k == 'conn':
                        self.ws.get_from_protocol(websocket).gs_conn = v
                        self.ws.add_ws_conn_to_set()

            if self.client_list_of_gs_conn_should_be_updated:
                response = json.dumps({'reload_peername':self.manager.list_gs_conn})
                for _ws in self.ws.send_to_subscribers(path):
                    yield from _ws.server_protocol.send(response)
                for _ws in self.ws.get_from_update_require():
                    response = json.dumps({'set_peername':_ws.gs_conn})
                    yield from _ws.server_protocol.send(response)
                self.client_list_of_gs_conn_should_be_updated = False

            if self.ws.get_from_protocol(websocket).packets:
                response = json.dumps(self.ws.get_from_protocol(websocket).packets)
                self.ws.get_from_protocol(websocket).packets = []
                for _ws in self.ws.send_to_subscribers(path):
                    yield from _ws.server_protocol.send(response)
            else:
                pass
            yield from asyncio.sleep(0.5)

    @asyncio.coroutine
    def ws_handler(self, websocket, path):
        self.ws.get_from_protocol(websocket).path = path
        if path == ('/'):
            yield from self.index(websocket, path)


class WebSocketServerProtocol(websockets.WebSocketServerProtocol):

    def connection_made(self, transport):
        self.ws_handler.ws.append_ws(Websocket(self))
        super().connection_made(transport)

    @asyncio.coroutine
    def recv(self):
        """
        This coroutine receives the next message.

        It returns a :class:`str` for a text frame and :class:`bytes` for a
        binary frame.

        Non blocking version
        """
        #Return any available message
        try:
            msg = self.messages.get_nowait()
            return msg
        except QueueEmpty:
            pass

    def connection_lost(self, exc):
        print('connection_lost : {}'.format(self))
        self.ws_handler.ws.remove_ws(self)
        super().connection_lost(exc)


def websocket_serve(loop, manager):
    ws_handler = WsHandler(manager)
    start_server = yield from websockets.serve(ws_handler,
        '0.0.0.0', 8765, klass=WebSocketServerProtocol, )
