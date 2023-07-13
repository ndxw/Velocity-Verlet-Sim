import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Solver import *

def showScreen():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all black)
        glLoadIdentity()
        iterate()
        glColor(1.0, 0.0, 0.0)
        draw_objects()
        glutSwapBuffers()

def draw_objects():
    resolution = 30

    glBegin(GL_POLYGON)
    for vertex in range(resolution):
        
        # TODO: draw circle around obj position
        vertex_x, vertex_y = 0, 0

        glVertex2d(vertex_x, vertex_y)
    glEnd()

def iterate():

    glViewport(0, 0, window_x, window_y)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_x, 0.0, window_y, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():

    # ball parameters
    radius = 50
    pos = Vec2D(500, 500)   # center of bounds
    vel = Vec2D(5.0, 5.0)
    acl = Vec2D(0.0, 0.0)

    # create objects
    ball = Circle(radius, pos, vel, acl)

    # init solver
    solver = Solver()
    solver.add_object(ball)


    glutInit() # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
    glutInitWindowSize(window_x, window_y)   # Set the width and height of your window
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
    wind = glutCreateWindow('OpenGL Coding Practice') # Give your window a title
    glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
    glutMainLoop()  # Keeps the window created above displaying/running in a loop

main()