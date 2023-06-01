import os

import requests
from appmodule import BaseModule

class PingModule(BaseModule):
    def run(self):
        for i in range(1000):
            requests.get(url = 'google.com')


def get_module():
    return PingModule