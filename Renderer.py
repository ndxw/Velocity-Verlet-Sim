
from math import *
from OpenGL.GL import *
from Solver import *

class Renderer:

    RESOLUTION = 30 # no. of sides on circle approximation

    @classmethod
    def render(cls, solver: Solver):

        # render bounding box
        bounds = solver.get_bounds()

        glColor(1.0, 1.0, 1.0)  # white

        glBegin(GL_QUADS)
        # draw unfilled rect
        glEnd()

        # render objects
        objects = solver.get_objects()

        glColor(1.0, 0.0, 0.0)  # red

        for object in objects:
            glBegin(GL_POLYGON)
            for vertex in range(cls.RESOLUTION):
                
                # draw circle around obj position
                vertex_x = object.radius * cos(vertex * 2 * pi / cls.RESOLUTION) + object.pos.x
                vertex_y = object.radius * sin(vertex * 2 * pi / cls.RESOLUTION) + object.pos.y

                glVertex2d(vertex_x, vertex_y)
            glEnd()