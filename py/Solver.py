from Object import Circle
from Bounds import RectBounds
from Grid import Grid
from Vec2D import Vec2D
from random import randrange
from time import sleep
from Timer import time_this
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

class Solver:

    def __init__(self, window_width, window_height):
        self.time = 0.0
        
        self.GRAVITY = Vec2D(0.0, -3000.0)
        self.BOUNDS = RectBounds(left=0, right=window_width, up=window_height, down=0)  # default 1000 x 1000 @ (0,0)
        self.FRAMERATE = 60
        self.SUBSTEPS = 4
        self.DT = 1 / self.FRAMERATE
        self.SUBDT = self.DT / float(self.SUBSTEPS)

        self.objects = []
        self.object_count = 0
        self.prev_spawn = 0.0                    # timestamp of previous ball spawned
        self.MAX_OBJECTS = 1000
        self.SPAWN_INTERVAL = 0.1                # in seconds
        self.OBJ_MAX_SIZE = 40
        self.OBJ_MIN_SIZE = 10

        self.WINDOW_W = window_width
        self.WINDOW_H = window_height
        self.grid = Grid(cell_size=self.OBJ_MAX_SIZE, window_width=window_width, window_height=window_height)

    def update_solver(self):

        for i in range(self.SUBSTEPS):
            self.apply_gravity()
            self.apply_bounds()
            self.apply_collisions()
            self.apply_coeff_restitution()
            self.update_objects(self.SUBDT)

        self.time += self.DT
        
    def add_object(self):
        self.objects.append(self.generate_ball())
        self.prev_spawn = self.time
        self.object_count += 1

    # Generates a ball with a random radius and mass
    def generate_ball(self):
        diameter = randrange(self.OBJ_MIN_SIZE, self.OBJ_MAX_SIZE, 5)
        mass = diameter
        pos = Vec2D(self.WINDOW_W * 0.25, self.WINDOW_H * 0.75)
        vel = Vec2D(2000.0, -10.0)
        # pos = Vec2D(randrange(0, self.WINDOW_W), randrange(0, self.WINDOW_H)) # testing Grid
        # vel = Vec2D(0.0, 0.0)   # testing Grid
        acl = Vec2D(0.0, 0.0)
        return Circle(diameter//2, pos, vel, acl, mass)
    
    # @time_this
    def apply_gravity(self):
        for object in self.objects:
            object.acl = self.GRAVITY

    # @time_this
    def apply_collisions(self):
        self.grid.partition_objects(self.objects)

        for k in range(len(self.grid.cells)):
            # don't iterate over edge cells
            if k < self.grid.height or k >= len(self.grid.cells)-self.grid.height or \
                (k % self.grid.height) in (0, self.grid.height-1): continue

            """ create a list of all objects in current cell and adjacent cells """
            objects = []
            objects += self.grid.cells[k]   # add all objects in current cell
            adj_cells = [k-self.grid.height-1, k-self.grid.height, k-self.grid.height+1, 
                         k-1, k+1,
                         k+self.grid.height-1, k+self.grid.height, k+self.grid.height+1]

            for cell in adj_cells:
                objects += self.grid.cells[cell]

            """ collision detection """
            for i in range(len(objects)):
                object1 = objects[i]
                for j in range(i+1, len(objects)):
                    object2 = objects[j]

                    pos_diff_12 = Vec2D.subtract(object1.pos, object2.pos)

                    if pos_diff_12.mag > object1.radius + object2.radius:
                        continue

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

                    vel_diff_21 = Vec2D.subtract(object2.vel, object1.vel)
                    pos_diff_21 = Vec2D.subtract(object2.pos, object1.pos)
                    divisor2 = pos_diff_21.mag * pos_diff_21.mag
                    mass_ratio2 = 2 * object1.mass / (object1.mass + object2.mass)
                    dot2 = Vec2D.dot(vel_diff_21, pos_diff_21)
                    scalar2 = mass_ratio2 * dot2 / divisor2
                    pos_diff_21_scaled = Vec2D.scale(pos_diff_21, scalar2)

                    '''===========================================================
                    Update object velocities
                    '''
                    object1.vel = Vec2D.subtract(object1.vel, pos_diff_12_scaled)
                    object2.vel = Vec2D.subtract(object2.vel, pos_diff_21_scaled)

                    '''===========================================================
                    Update positions by shifting each object by half the overlap
                    in opposite directions along the collision axis
                    '''
                    overlap = object1.radius + object2.radius - pos_diff_12.mag
                    pos_diff_21 = Vec2D.subtract(object2.pos, object1.pos)

                    update_pos1 = Vec2D.scale(pos_diff_12, 0.5 * overlap / pos_diff_12.mag)
                    object1.pos = Vec2D.add(object1.pos, update_pos1)

                    update_pos2 = Vec2D.scale(pos_diff_21, 0.5 * overlap / pos_diff_21.mag)
                    object2.pos = Vec2D.add(object2.pos, update_pos2)

                    # set collision status for velocity scaling later
                    object1.collided = True
                    object2.collided = True
               
        self.grid.cells = self.grid.generate_cells()

    def apply_coeff_restitution(self):
        for object in self.objects:
            if object.collided:
                object.vel = Vec2D.scale(object.vel, object.COLLISION_COEFF)
                object.collided = False


    # @time_this
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

    # @time_this
    def update_objects(self, dt):
        for object in self.objects:
            object.update(dt)
