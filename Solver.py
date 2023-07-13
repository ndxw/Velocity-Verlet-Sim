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
    
    def get_bounds(self):
        return self.bounds
    
    def apply_gravity(self):
        pass

    def apply_collisions(self):
        pass

    def apply_bounds(self):
        pass

    def update_objects(self):
        pass

    def update_solver(self):

        self.apply_gravity()
        self.apply_collisions()
        self.apply_bounds()
        self.update_objects()
    