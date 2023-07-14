import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Solver import *
from Renderer import *
from time import sleep, perf_counter

window_x, window_y = 1500, 1500

 # ball parameters
radius = 50
pos = Vec2D(750, 750)
vel = Vec2D(10000.0, 5000.0)
acl = Vec2D(0.0, 0.0)

# create objects
ball = Circle(radius, pos, vel, acl)

# init solver
solver = Solver()
solver.add_object(ball)

def showScreen():

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all black)
        glLoadIdentity()
        iterate()

        solver.update_solver()
        Renderer.render(solver)

        glutSwapBuffers()
        sleep(0.015)    # should be solver.dt (framerate period)

def iterate():

    glViewport(0, 0, window_x, window_y)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_x, 0.0, window_y, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():

    glutInit() # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
    glutInitWindowSize(window_x, window_y)   # Set the width and height of your window
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
    wind = glutCreateWindow('OpenGL Coding Practice') # Give your window a title
    glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
    glutMainLoop()  # Keeps the window created above displaying/running in a loop

main()