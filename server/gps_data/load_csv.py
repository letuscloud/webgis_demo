import csv
import random
import os

car_gps_store = {}


class CarGPSTrace(object):

    def __init__(self, car_id):
        self.car_id = car_id
        self.len = 0
        self.gps = []

    def add_pos(self, lat, lng):
        self.gps.append([lat, lng])
        self.len += 1

    def get_pos(self, index):
        if index < self.len:
            return self.gps[index]
        return None


def init_gps_data():
    csv_file = os.path.join(os.path.dirname(__file__), "guangzhou.csv")
    with open(csv_file, newline='') as fd:
        reader = csv.DictReader(fd)
        for row in reader:
            car_id = row['id']
            lat = row['lat']
            lng = row['lng']

            if car_id in car_gps_store:
                car_gps_info = car_gps_store[car_id]
            else:
                car_gps_info = CarGPSTrace(car_id)
                car_gps_store[car_id] = car_gps_info

            car_gps_info.add_pos(lat, lng)


def get_gps_pos(car_id, index):
    car_gps_info = car_gps_store[car_id]

    return car_gps_info.get_pos(index)


def get_random_car_ids(cnt):
    print("len(car_gps_store) --> ", len(car_gps_store))

    if cnt > len(car_gps_store):
        raise Exception("gps list count exceeded")
    return random.sample(car_gps_store.keys(), cnt)


init_gps_data()
