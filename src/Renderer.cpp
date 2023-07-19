#include "Renderer.h"

static void Renderer::render(Solver &solver)
{
    // render bounding box
    RectBounds& bounds = solver.getBounds();

    glColor(1.0, 1.0, 1.0);

    glBegin(GL_QUADS);
    glVertex2d(vertexX, vertexY);
    glVertex2d(vertexX, vertexY);
    glVertex2d(vertexX, vertexY);
    glVertex2d(vertexX, vertexY);
    glEnd();

    //=====================================================================

    vector<Object>& objects = solver.getObjects();
    float vectorScale = 0.02;
    int lineWidth = 3;

    for (int i = 0; i < objects.size(); i++)
    {
        // render objects
        glColor(object[i].colour[0], object[i].colour[1], object[i].colour[2]);

        glBegin(GL_POLYGON);
        for (int vertex = 0; vertex < RESOLUTION)
        {
            float vertexX = object[i].radius * cos(vertex * 2 * pi / RESOLUTION) + object[i].pos.x;
            float vertexY = object[i].radius * sin(vertex * 2 * pi / RESOLUTION) + object[i].pos.y;
            glVertex2d(vertexX, vertexY);
        }
        glEnd()

        // render object velocity vectors
        
    }
}