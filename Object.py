from random import random
from Vec2D import Vec2D

class Object:

    def __init__(self, pos: Vec2D, vel: Vec2D, acl: Vec2D, mass: float):
        self.pos = pos
        self.vel = vel
        self.acl = acl
        self.mass = mass
        self.COLLISION_COEFF = 0.75

        red = random()
        green = random()
        blue = random()
        self.colour = (red, green, blue)

    def update(self, dt):

        # calculate new position
        vdt = Vec2D.scale(self.vel, dt)
        adtdt = Vec2D.scale(self.acl, (dt*dt) * 0.5)
        self.pos = Vec2D.add(self.pos, vdt, adtdt)

        # calculate new velocity
        adt = Vec2D.scale(self.acl, dt)
        self.vel = Vec2D.add(self.vel, adt)


class Circle(Object):

    def __init__(self, radius: float, pos: Vec2D, vel: Vec2D, acl: Vec2D, mass: float):
        super().__init__(pos, vel, acl, mass)
        self.radius = radius

    def get_radius(self):
        return self.radius