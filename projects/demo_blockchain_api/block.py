import datetime
import hashlib
import json

import os
os.environ.setdefault('APPENGINE_RUNTIME',"0")
print(os.path.expanduser("~/Developer"))
class Block:
    def __init__(self, data, previous_hash):
        # self.hash = self.calculate_hash()
        self.data = data
        self.previous_hash = previous_hash
        self.time_stamp = str(datetime.datetime.now())


def create_block(index, data):
    # starting from second block
    block = {
        "index": index,
        "timestamp": str(datetime.datetime.now()),
        "data": data,
        "previous_hash": "0",
    }
