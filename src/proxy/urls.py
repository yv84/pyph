import asyncio

from flask import Flask, render_template


def flask_route(loop, manager):
    app = Flask(__name__)
    app.debug = True

    @app.route('/')
    def index():
        response = '<h1>Index page</h1><a href="/async">async</a>, <a href="/demo">async-demo</a>, <a href="/flask">flask</a>' + \
          '<p>' + repr(loop) + '</p>' + '<p>' + repr(app) + '</p>' + \
          '<p>' + repr(manager.data) + '</p>' +\
          repr(b''.join([b'<p><ol><li>',
              (b'</li><li>'.join(manager.packets)),
              b'</li></ol></p>']))
        return response
     
    @app.route('/demo')
    def demo():
        return '''
    <script>
    var source = new EventSource('/async');
    source.onmessage = function(event) { document.write(event.data + '<hr />'); }
    </script>
    '''
     
    # inheriting from app.response_class is critical -- otherwise, the `if not
    # isinstance(rv, self.response_class):` line in flask.app.Flask.make_response
    # triggers, we get fed through force_type, and pushed through
    # flask.test.Client.run_wsgi_app, which does not run this wsgi app as it
    # intends to be run
    class EventSender(app.response_class):
        @asyncio.coroutine
        def __call__(self, environ, start_response):
            write = start_response('200 ok', [('content-type', 'text/event-stream')])
            write(b"data: welcome\n\n")
            for x in range(20):
                yield from asyncio.sleep(2)
                write(("data: hello world %d\n\n"%x).encode('ascii'))
            return []
     
        def __init__(self): pass
        __enter__ = None
        close = None
        call_on_close = None
     
    @app.route('/async')
    def async():
        return EventSender()
     
    @app.route('/flask')
    def flask():
        return render_template('some_flask_template.html')
    return app