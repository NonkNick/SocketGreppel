import json
from json import JSONEncoder
from random import seed
from dcMotor import dcMotor
import random
import json
import socketConnector

sc = socketConnector.SocketConnector()

class greppelState:
    def __init__(self, temp, num):
        self.temp = temp
        self.num = num
        self.dc1 = 0,
        self.dc2 = 0,
        self.dc3 = 0,
        self.dc4 = 0,
        self.ran5 = random.random()
        # self.sc = socketConnector.SocketConnector()
    def getState(self):
        sc.getState()
        self.dc1 = sc.getdc1()
        self.dc2 = sc.getdc2()
        self.dc3 = sc.getdc3()
        self.dc4 = sc.getdc4()


class greppelStateEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__