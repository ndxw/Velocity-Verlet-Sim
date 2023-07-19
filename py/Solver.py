from Object import *
from Bounds import *

class Solver:

    def __init__(self):
        self.time = 0.0
        self.objects = []
        self.object_count = 0
        self.GRAVITY = Vec2D(0.0, -3000.0)
        self.BOUNDS = RectBounds()  # default 1000 x 1000 @ (0,0)
        self.FRAMERATE = 60
        self.SUBSTEPS = 2
        self.DT = 1 / self.FRAMERATE
        self.SUBDT = self.DT / float(self.SUBSTEPS)
        self.MAX_OBJECTS = 50

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

                    # print(f'Positions @ impact:\nObject 1: {object1.pos.to_string()}\nObject 2: {object2.pos.to_string()}')
                    # print(f'Masses:\nObject 1: {object1.mass}\nObject 2: {object2.mass}\n')

                    # print(f'Object 1 old velocity: {object1.vel.to_string()}')

                    '''=======================================================================
                    Calculate new velocities using equations for two-dimensional 
                    collision with two moving objects

                    Equations in vector representation can be
                    found @ https://en.wikipedia.org/wiki/Elastic_collision
                    '''
                    vel_diff_12 = Vec2D.subtract(object1.vel, object2.vel)
                    pos_diff_12 = Vec2D.subtract(object1.pos, object2.pos)
                    divisor1 = pos_diff_12.mag * pos_diff_12.mag
                    mass_ratio1 = 2 * object2.mass / (object1.mass + object2.mass)
                    dot1 = Vec2D.dot(vel_diff_12, pos_diff_12)
                    scalar1 = mass_ratio1 * dot1 / divisor1
                    pos_diff_12_scaled = Vec2D.scale(pos_diff_12, scalar1)

                    # print(f'\t{"vel_diff_12":<18} = {vel_diff_12.to_string()}\n',
                    #     f'\t{"pos_diff_12":<18} = {pos_diff_12.to_string()}\n',
                    #     f'\t{"divisor1":<18} = {divisor1}\n',
                    #     f'\t{"mass_ratio1":<18} = {mass_ratio1}\n',
                    #     f'\t{"dot1":<18} = {dot1}\n',
                    #     f'\t{"scalar1":<18} = {scalar1}\n',
                    #     f'\t{"pos_diff_12_scaled":<18} = {pos_diff_12_scaled.to_string()}')
                          
                    # print(f'\nObject 2 old velocity: {object2.vel.to_string()}')

                    vel_diff_21 = Vec2D.subtract(object2.vel, object1.vel)
                    pos_diff_21 = Vec2D.subtract(object2.pos, object1.pos)
                    divisor2 = pos_diff_21.mag * pos_diff_21.mag
                    mass_ratio2 = 2 * object1.mass / (object1.mass + object2.mass)
                    dot2 = Vec2D.dot(vel_diff_21, pos_diff_21)
                    scalar2 = mass_ratio2 * dot2 / divisor2
                    pos_diff_21_scaled = Vec2D.scale(pos_diff_21, scalar2)

                    # print(f'\t{"vel_diff_21":<18} = {vel_diff_21.to_string()}\n',
                    #       f'\t{"pos_diff_21":<18} = {pos_diff_21.to_string()}\n',
                    #       f'\t{"divisor2":<18} = {divisor2}\n',
                    #       f'\t{"mass_ratio2":<18} = {mass_ratio2}\n',
                    #       f'\t{"dot2":<18} = {dot2}\n',
                    #       f'\t{"scalar2":<18} = {scalar2}\n',
                    #       f'\t{"pos_diff_21_scaled":<18} = {pos_diff_21_scaled.to_string()}')
                    
                    # print(f'\nObject 1 new velocity: {object1.vel.to_string()}')
                    # print(f'Object 2 new velocity: {object2.vel.to_string()}\n')

                    '''===========================================================
                    Update object velocities
                    '''
                    object1.vel = Vec2D.subtract(object1.vel, pos_diff_12_scaled)
                    object1.vel = Vec2D.scale(object1.vel, object1.COLLISION_COEFF)
                    object2.vel = Vec2D.subtract(object2.vel, pos_diff_21_scaled)
                    object2.vel = Vec2D.scale(object2.vel, object2.COLLISION_COEFF)

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
               
    def apply_bounds(self):

        for object in self.objects:

            # collision with right wall
            if object.pos.x + object.radius > self.BOUNDS.right:
                object.pos.x = self.BOUNDS.right - object.radius
                object.vel.mirror_y()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            # collision with left wall
            elif object.pos.x - object.radius < self.BOUNDS.left:
                object.pos.x = self.BOUNDS.left + object.radius
                object.vel.mirror_y()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            # collision with ceiling
            if object.pos.y + object.radius > self.BOUNDS.up:
                object.pos.y = self.BOUNDS.up - object.radius
                object.vel.mirror_x()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

            # collision with floor
            elif object.pos.y - object.radius < self.BOUNDS.down:
                object.pos.y = self.BOUNDS.down + object.radius
                object.vel.mirror_x()
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)

    def update_objects(self, dt):
        for object in self.objects:
            object.update(dt)

    
    