import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Solver import *
from Renderer import *
from time import sleep
from random import randrange

WINDOW_W, WINDOW_H = 1000, 1000
SPAWN_INTERVAL = 0.5
prev_spawn = 0.0

# init solver
solver = Solver()

# Generates a ball with a random radius and mass
def generate_ball():
     radius = randrange(50, 100, 10)
     mass = radius
     pos = Vec2D(WINDOW_W * 0.25, WINDOW_H * 0.75)
     vel = Vec2D(4000.0, 1000.0)
     acl = Vec2D(0.0, 0.0)
     return Circle(radius, pos, vel, acl, mass)

def showScreen():
    global prev_spawn

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all black)
    glLoadIdentity()
    iterate()

    solver.update_solver()
    Renderer.render(solver)

    if solver.time - prev_spawn >= SPAWN_INTERVAL and solver.object_count < solver.MAX_OBJECTS:
        solver.add_object(generate_ball())
        prev_spawn = solver.time

    glutSwapBuffers()
    sleep(0.015)    # should be solver.dt (framerate period)

def iterate():

    glViewport(0, 0, WINDOW_W, WINDOW_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_W, 0.0, WINDOW_H, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():

    glutInit() # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
    glutInitWindowSize(WINDOW_W, WINDOW_H)   # Set the width and height of your window
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
    wind = glutCreateWindow('Velocity-Verlet Physics Simulation') # Give your window a title
    glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
    glutMainLoop()  # Keeps the window created above displaying/running in a loop

main()