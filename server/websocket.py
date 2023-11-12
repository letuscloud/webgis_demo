import sys
import time
import json
import random
import threading
from flask import Blueprint
# from server.gps_data.load_csv import car_gps_data
from gps_data import get_random_car_ids, get_gps_pos
ws = Blueprint('panda', __name__, url_prefix="/")

ws_connection = {}

def gen_connection_id():
    connection_id = random.randint(1, sys.maxsize )
    return str(connection_id)

@ws.route('/pull', websocket=True)
def on_panda(socket):
    is_error = False
    print("on connect")

    connection_id = gen_connection_id()
    ws_connection[connection_id] = socket

    while not socket.closed:
        try:
            message = socket.receive()
            if message:
                print(message)

            start_send_data(socket)

        except Exception as e:
            print("socket error???")
            is_error = True
            print(e)
    ws_connection.pop(connection_id)
    print("return", is_error)
    return is_error


def start_send_data(ws_session):
    t = threading.Thread(target=thread_function, args=(ws_session,))
    t.start()



def thread_function(ws_session):



    i = 0



    car_ids = get_random_car_ids(10)

    while True:
        payload = []
        for car_id in car_ids:
            pos = get_gps_pos(car_id, i)
            if pos:
                payload.append([car_id, pos[0], pos[1]])

        msg = json.dumps(payload)

        print("msg: ", msg)

        ws_session.send(msg)
        i += 1
        time.sleep(1)




