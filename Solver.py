from Object import *
from Bounds import *

class Solver:

    def __init__(self):
        self.objects = []
        self.GRAVITY = Vec2D(0.0, -3000.0)
        self.bounds = Bounds(250, 1250, 1250, 250)  # default 1000 x 1000 @ (0,0)
        self.framerate = 60
        self.dt = 1 / self.framerate

    def add_object(self, obj: Object):
        self.objects.append(obj)

    # def get_objects(self):
    #     return self.objects
    
    # def get_bounds(self):
    #     return self.bounds
    
    # def get_dt(self):
    #     return self.dt
    
    def apply_gravity(self):
        for object in self.objects:
            object.acl = self.GRAVITY

    def apply_collisions(self):
        pass

    def apply_bounds(self):
        '''
        ISSUES
        - Only scaling single axis results in frictionless floor
        - Scaling both axes results in unnatural behaviour when colliding with wall and ceiling
        - Object phases through walls at high speeds (maybe use pos at t+1 in collision condition)
        - "Jittering" when objects at rest on floor
        '''
        for object in self.objects:
            if object.pos.x + object.radius > self.bounds.right:
                object.pos.x = self.bounds.right - object.radius
                object.vel.x *= -object.COLLISION_COEFF
                # object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            elif object.pos.x - object.radius < self.bounds.left:
                object.pos.x = self.bounds.left + object.radius
                object.vel.x *= -object.COLLISION_COEFF
                # object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            if object.pos.y + object.radius > self.bounds.up:
                object.pos.y = self.bounds.up - object.radius
                object.vel.y *= -object.COLLISION_COEFF
                # object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            elif object.pos.y - object.radius < self.bounds.down:
                object.pos.y = self.bounds.down + object.radius
                object.vel.y *= -object.COLLISION_COEFF
                # object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

    def update_objects(self, dt):
        for object in self.objects:
            object.update(dt)

    def update_solver(self):
        '''
        - Applying bounds after updating objects seems to have mostly fixed phasing 
        through walls at high speeds
        '''
        self.apply_gravity()
        self.apply_collisions()
        self.update_objects(self.dt)
        self.apply_bounds()
    