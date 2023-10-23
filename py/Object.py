from random import uniform
from Vec2D import Vec2D

class Object:

    def __init__(self, pos: Vec2D, vel: Vec2D, acl: Vec2D, mass: float):
        self.pos = pos
        self.vel = vel
        self.acl = acl
        self.mass = mass
        self.collided = False
        self.COLLISION_COEFF = 0.8

        red = uniform(0.0, 0.8)
        green = uniform(0.0, 0.8)
        blue = uniform(0.0, 0.8)
        self.colour = (red, green, blue)

    def update(self, dt):

        '''=========================================================
        Equations for Velocity-Verlet integration can be
        found @ https://en.wikipedia.org/wiki/Verlet_integration
        '''

        # calculate v(t+0.5*dt)
        half_adt = Vec2D.scale(self.acl, dt*0.5)
        half_vel = Vec2D.add(self.vel, half_adt)

        # calculate new position
        half_vdt = Vec2D.scale(half_vel, dt)
        self.pos = Vec2D.add(self.pos, half_vdt)

        # calculate new velocity
        self.vel = Vec2D.add(half_vel, half_adt)


class Circle(Object):

    def __init__(self, radius: float, pos: Vec2D, vel: Vec2D, acl: Vec2D, mass: float):
        super().__init__(pos, vel, acl, mass)
        self.radius = radius

    def get_radius(self):
        return self.radius