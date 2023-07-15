from Object import *
from Bounds import *

class Solver:

    def __init__(self):
        self.time = 0.0
        self.objects = []
        self.object_count = 0
        self.GRAVITY = Vec2D(0.0, -3000.0)
        self.BOUNDS = Bounds()  # default 1000 x 1000 @ (0,0)
        self.FRAMERATE = 60
        self.SUBSTEPS = 5
        self.DT = 1 / self.FRAMERATE
        self.SUBDT = self.DT / float(self.SUBSTEPS)
        self.MAX_OBJECTS = 8

    def update_solver(self):

        for i in range(self.SUBSTEPS):
            self.apply_gravity()
            self.apply_collisions()
            self.update_objects(self.SUBDT)
            self.apply_bounds()

        self.time += self.DT
        
    def add_object(self, obj: Object):
        self.objects.append(obj)
        self.object_count += 1

    # def get_objects(self):
    #     return self.objects
    
    # def get_bounds(self):
    #     return self.BOUNDS
    
    # def get_dt(self):
    #     return self.DT
    
    def apply_gravity(self):
        for object in self.objects:
            object.acl = self.GRAVITY

    def apply_collisions(self):
        for i in range(len(self.objects)):
            object1 = self.objects[i]
            for j in range(i+1, len(self.objects)):
                object2 = self.objects[j]

                pos_diff_12 = Vec2D.subtract(object1.pos, object2.pos)

                if pos_diff_12.mag < object1.radius + object2.radius:
                    '''
                    Update positions by shifting each object by half the overlap
                    in opposite directions along the collision axis
                    '''
                    overlap = object1.radius + object2.radius - pos_diff_12.mag
                    pos_diff_21 = Vec2D.subtract(object2.pos, object1.pos)

                    update_pos1 = Vec2D.scale(pos_diff_12, 0.5 * overlap / pos_diff_12.mag)
                    object1.pos = Vec2D.add(object1.pos, update_pos1)

                    update_pos2 = Vec2D.scale(pos_diff_21, 0.5 * overlap / pos_diff_21.mag)
                    object2.pos = Vec2D.add(object2.pos, update_pos2)

                    '''
                    Update velocities using equations for two-dimensional collision
                    with two moving objects
                    '''
                    vel_diff_12 = Vec2D.subtract(object1.vel, object2.vel)
                    # pos_diff_12 already calculated
                    divisor1 = pos_diff_12.mag * pos_diff_12.mag
                    mass_ratio1 = 2 * object2.mass / (object1.mass + object2.mass)
                    dot1 = Vec2D.dot(vel_diff_12, pos_diff_12)
                    dot1 *= mass_ratio1 / divisor1
                    pos_diff_12 = Vec2D.scale(pos_diff_12, dot1)
                    object1.vel = Vec2D.subtract(object1.vel, pos_diff_12)
                    object1.vel = Vec2D.scale(object1.vel, 0.98)

                    vel_diff_21 = Vec2D.subtract(object2.vel, object1.vel)
                    # pos_diff_21 already calculated
                    divisor2 = pos_diff_21.mag * pos_diff_21.mag
                    mass_ratio2 = 2 * object1.mass / (object1.mass + object2.mass)
                    dot2 = Vec2D.dot(vel_diff_21, pos_diff_21)
                    dot2 *= mass_ratio2 / divisor2
                    pos_diff_21 = Vec2D.scale(pos_diff_21, dot2)
                    object2.vel = Vec2D.subtract(object2.vel, pos_diff_21)
                    object2.vel = Vec2D.scale(object2.vel, 0.98)


    def apply_bounds(self):
        '''
        ISSUES
        - Only scaling single axis results in frictionless floor
        - Scaling both axes results in unnatural behaviour when colliding with wall and ceiling
        - Object phases through walls at high speeds (maybe use pos at t+1 in collision condition)
        - "Jittering" when objects at rest on floor
        '''
        for object in self.objects:
            if object.pos.x + object.radius > self.BOUNDS.right:
                object.pos.x = self.BOUNDS.right - object.radius
                object.vel.mirror_y()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            elif object.pos.x - object.radius < self.BOUNDS.left:
                object.pos.x = self.BOUNDS.left + object.radius
                object.vel.mirror_y()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            if object.pos.y + object.radius > self.BOUNDS.up:
                object.pos.y = self.BOUNDS.up - object.radius
                object.vel.mirror_x()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            elif object.pos.y - object.radius < self.BOUNDS.down:
                object.pos.y = self.BOUNDS.down + object.radius
                object.vel.mirror_x()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

    def update_objects(self, dt):
        for object in self.objects:
            object.update(dt)

    
    