
from math import *
from OpenGL.GL import *
from Solver import *

class Renderer:

    RESOLUTION = 20 # no. of sides on circle approximation

    @classmethod
    def render(cls, solver: Solver):

        # render bounding box
        glColor(1.0, 1.0, 1.0)  # white

        glBegin(GL_QUADS)
        glVertex2d(solver.bounds.left, solver.bounds.down)
        glVertex2d(solver.bounds.right, solver.bounds.down)
        glVertex2d(solver.bounds.right, solver.bounds.up)
        glVertex2d(solver.bounds.left, solver.bounds.up)
        glEnd()

        # render objects
        glColor(1.0, 0.0, 0.0)  # red

        for object in solver.objects:
            glBegin(GL_POLYGON)
            for vertex in range(cls.RESOLUTION):
                
                # draw circle around obj position
                vertex_x = object.radius * cos(vertex * 2 * pi / cls.RESOLUTION) + object.pos.x
                vertex_y = object.radius * sin(vertex * 2 * pi / cls.RESOLUTION) + object.pos.y

                glVertex2d(vertex_x, vertex_y)
            glEnd()