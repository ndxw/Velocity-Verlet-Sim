from Vec2D import Vec2D

class Object:

    def __init__(self, pos: Vec2D, vel: Vec2D, acl: Vec2D):
        self.pos = pos
        self.vel = vel
        self.acl = acl

    def update(self, pos: Vec2D, vel: Vec2D, acl: Vec2D):
        self.pos = pos
        self.vel = vel
        self.acl = acl

class Circle(Object):

    def __init__(self, radius: float, pos: Vec2D, vel: Vec2D, acl: Vec2D):
        super().__init__(pos, vel, acl)
        self.radius = radius