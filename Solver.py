from Object import *
from Bounds import *

class Solver:

    def __init__(self):
        self.objects = []
        self.gravity = 10
        self.bounds = Bounds()  # default 1000 x 1000 @ (0,0)
        self.framerate = 60
        self.dt = 1 / self.framerate

    def add_object(self, obj: Object):
        self.objects.append(obj)

    def get_objects(self):
        return self.objects

    