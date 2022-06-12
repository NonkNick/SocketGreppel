import json
from json import JSONEncoder
from random import seed
import random
import json
import socketConnector

sc = socketConnector.SocketConnector()

class greppelState:
    def __init__(self):
        self.json = ""
        # self.temp = temp
        # self.num = num
        # self.dc1 = 0,
        # self.dc2 = 0,
        # self.dc3 = 0,
        # self.dc4 = 0,
        # self.ran5 = random.random()
        # # self.sc = socketConnector.SocketConnector()
    def getState(self):
        sc.getState()
        # self.dc1 = sc.getdc1()
        # self.dc2 = sc.getdc2()
        # self.dc3 = sc.getdc3()
        # self.dc4 = sc.getdc4()
        self.json = sc.getJson()
        # self.dc1 = random.random()
        # self.dc2 = random.random()
        # self.dc3 = random.random()
        # self.dc4 = random.random()
    def getJson(self):
        return self.json

# class greppelStateEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__