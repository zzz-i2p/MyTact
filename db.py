import json
import os

DB_FILE = "data.json"

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILE) 

def load():
    with open(PATH, 'rb') as _fp:
        data = json.load(_fp)
    return data

def insert(data):
    with open(PATH, 'wb') as _fp:
        json.dump(data, _fp)