import os
import asyncio

from flask import Flask, render_template
from flask import Flask, current_app, send_file, render_template_string
from werkzeug.exceptions import NotFound


def flask_route(loop, manager):

    app = Flask(__name__)
    app.debug = True

    # http://thomassileo.com/blog/2013/12/12/using-yeoman-with-flask/
    @app.route('/', defaults={'path': 'index.html'})
    @app.route('/<path:path>')
    def serve_index(path):
        flask_yeoman_debug = int(os.environ.get('FLASK_YEOMAN_DEBUG', True))
        fpath = '../web_client/dist'
        # While developing, we serve the app directory
        if flask_yeoman_debug:
            fpath = '../web_client/app'

        root_path = current_app.root_path
        default_path = os.path.join(root_path, fpath)

        default_path_abs = os.path.join(default_path, path)

        if os.path.isfile(default_path_abs):
            if path == 'index.html':
                # If index.html is requested, we inject the Flask current_app config
                return render_template_string(open(default_path_abs).read(),
                                              config=current_app.config)
            return send_file(default_path_abs)

        # While development, we must check the .tmp dir as fallback
        if flask_yeoman_debug:
            # The .tmp dir is used by compass and for the template file
            alt_path = os.path.join(root_path, '../web_client/.tmp')
            alt_path_abs = os.path.join(alt_path, path)
            if os.path.isfile(alt_path_abs):
                return send_file(alt_path_abs)

        if flask_yeoman_debug:
            # bower_components
            alt_path = os.path.join(root_path, '../web_client/')
            alt_path_abs = os.path.join(alt_path, path)
            if os.path.isfile(alt_path_abs):
                return send_file(alt_path_abs)

        raise NotFound()


    return app
