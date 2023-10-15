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
        glVertex2d(solver.BOUNDS.left, solver.BOUNDS.down)
        glVertex2d(solver.BOUNDS.right, solver.BOUNDS.down)
        glVertex2d(solver.BOUNDS.right, solver.BOUNDS.up)
        glVertex2d(solver.BOUNDS.left, solver.BOUNDS.up)
        glEnd()

        # render objects
        for object in solver.objects:

            glColor(object.colour[0], object.colour[1], object.colour[2])

            glBegin(GL_POLYGON)
            for vertex in range(cls.RESOLUTION):
                
                # draw circle around object position
                vertex_x = object.radius * cos(vertex * 2 * pi / cls.RESOLUTION) + object.pos.x
                vertex_y = object.radius * sin(vertex * 2 * pi / cls.RESOLUTION) + object.pos.y

                glVertex2d(vertex_x, vertex_y)
            glEnd()

        # render object velocity vectors
        vector_scale = 0.02
        line_width = 3

        for object in solver.objects:

            glColor(1-object.colour[0], 1-object.colour[1], 1-object.colour[2])
            glLineWidth(line_width)

            glBegin(GL_LINES)
            glVertex2d(object.pos.x, object.pos.y)
            glVertex2d(object.pos.x + vector_scale * object.vel.x, object.pos.y + vector_scale * object.vel.y)
            glEnd()

        # render grid
        line_width = 1

        glColor(0, 0, 0)
        glLineWidth(line_width)

        # horizonal lines
        for i in range(solver.grid.cell_size, solver.WINDOW_H, solver.grid.cell_size):
            glBegin(GL_LINES)
            glVertex2d(0, i)
            glVertex2d(solver.WINDOW_W, i)
            glEnd()
        # vertical lines
        for i in range(solver.grid.cell_size, solver.WINDOW_W, solver.grid.cell_size):
            glBegin(GL_LINES)
            glVertex2d(i, 0)
            glVertex2d(i, solver.WINDOW_H)
            glEnd()