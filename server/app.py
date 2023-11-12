from __future__ import absolute_import

import os
from flask import Flask
from flask import redirect, url_for
from flask_cors import CORS
from flask_sockets import Sockets
from websocket import ws

app = Flask(__name__, static_url_path='/m')
sockets = Sockets(app)

sockets.register_blueprint(ws)
CORS(app)


@app.route("/")
def index():
    return "xxxxxxxxxx"





def start_app(falcon_port):
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    # app.debug = True

    server_host = "0.0.0.0"

    server_falcon = pywsgi.WSGIServer((server_host, falcon_port), app, handler_class=WebSocketHandler)


    server_falcon.serve_forever()


if __name__ == '__main__':
    start_app(8080)