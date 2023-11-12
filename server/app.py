from __future__ import absolute_import

import os
from flask_cors import CORS
from flask_sockets import Sockets
from flask import Flask, send_from_directory
from websocket import ws

file_path = os.path.dirname(os.path.abspath(__file__))
proj_path = os.path.dirname(file_path)

static_path = os.path.join(proj_path, 'ui')

app = Flask(__name__, static_url_path='/', static_folder=static_path)
sockets = Sockets(app)

sockets.register_blueprint(ws)
CORS(app)


@app.route('/')
def index():
    return send_from_directory(static_path, 'src/demo.html')


def start_app(falcon_port):
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    # app.debug = True
    server_host = "0.0.0.0"
    server_falcon = pywsgi.WSGIServer((server_host, falcon_port), app, handler_class=WebSocketHandler)
    server_falcon.serve_forever()


if __name__ == '__main__':
    start_app(8080)
