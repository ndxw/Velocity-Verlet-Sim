#include "../include/Renderer.h"
#include <cmath>

#define PI acos(-1)

void Renderer::render(Solver &solver)
{
    // render bounding box
    RectBounds bounds = solver.getBounds();

    glColor3f(1.0, 1.0, 1.0);

    glBegin(GL_QUADS);
    glVertex2d(bounds.left, bounds.down);
    glVertex2d(bounds.right, bounds.down);
    glVertex2d(bounds.right, bounds.up);
    glVertex2d(bounds.left, bounds.up);
    glEnd();

    //=====================================================================

    std::vector<Circle>& objects = solver.getObjects();
    float vectorScale = 0.02;
    int lineWidth = 3;

    for (int i = 0; i < objects.size(); i++)
    {
        Circle& obj = objects[i];
        float red = obj.colour[0];
        float green = obj.colour[1];
        float blue = obj.colour[2];

        // render objects
        glColor3f(red, green, blue);

        glBegin(GL_POLYGON);
        for (int vertex = 0; vertex < RESOLUTION; vertex++)
        {
            float vertexX = obj.radius * cos(vertex * 2 * PI / RESOLUTION) + obj.pos.x();
            float vertexY = obj.radius * sin(vertex * 2 * PI / RESOLUTION) + obj.pos.y();
            glVertex2d(vertexX, vertexY);
        }
        glEnd();

        // render object velocity vectors
        glColor3f(1 - red, 1 - green, 1 - blue);
        glLineWidth(lineWidth);

        glBegin(GL_LINES);
        glVertex2d(obj.pos.x(), obj.pos.y());
        glVertex2d(obj.pos.x() + vectorScale * obj.vel.x(), obj.pos.y() + vectorScale * obj.vel.y());
        glEnd();
    }
}