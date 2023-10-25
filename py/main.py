import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Solver import *
from Renderer import *
from Timer import time_this
from time import sleep, perf_counter, perf_counter_ns
from random import randrange
from multiprocessing import freeze_support

WINDOW_W, WINDOW_H = 700, 700

solver = Solver(WINDOW_W, WINDOW_H)
prev_frame_time = perf_counter()

def showScreen():
    global prev_frame_time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all black)
    glLoadIdentity()
    iterate()

    solver.update_solver()
    Renderer.render(solver)

    # TODO: object addition with mouse
    if solver.time - solver.prev_spawn >= solver.SPAWN_INTERVAL and solver.object_count < solver.MAX_OBJECTS:
        solver.add_object()
        
    glutSwapBuffers()
    
    while(perf_counter()-prev_frame_time < solver.DT):
        continue
    prev_frame_time = perf_counter()

# @time_this
def iterate():

    glViewport(0, 0, WINDOW_W, WINDOW_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_W, 0.0, WINDOW_H, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():

    glutInit()                              # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA)          # Set the display mode to be colored
    glutInitWindowSize(WINDOW_W, WINDOW_H)  # Set the width and height of your window
    glutInitWindowPosition(0, 0)            # Set the position at which this windows should appear
    wind = glutCreateWindow('Velocity-Verlet Physics Simulation') # Give your window a title
    glutDisplayFunc(showScreen)             # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)                # Draw any graphics or shapes in the showScreen function at all times
    glutMainLoop()                          # Keeps the window created above displaying/running in a loop

if __name__ == '__main__':
    main()