#include "../include/Solver.h"

Solver::Solver()
{
    time = 0.0;
    objects.clear(); objects.reserve(MAX_OBJECTS);
}

Solver::~Solver()
{
    
}

void Solver::applyGravity()
{
    for (int i = 0; i < objects.size(); i++)
    {
        objects[i].acl = GRAVITY;
    }
}

void Solver::applyCollisions()
{
    for (int i = 0; i < objects.size(); i++)
    {
        Circle &obj1 = objects[i];

        for (int j = i+1; j < objects.size(); j++)
        {
            Circle &obj2 = objects[j];
            Vec2D posDiff12 = obj1.pos - obj2.pos;

            if (posDiff12.length() < obj1.radius + obj2.radius)
            {
                /*
                Calculate new velocities using equations for two-dimensional 
                collision with two moving objects

                Equations in vector representation can be
                found @ https://en.wikipedia.org/wiki/Elastic_collision
                */
                float dot1 = Vec2D::dot(obj1.vel - obj2.vel, posDiff12);
                float massRatio1 = 2 * obj1.mass / (obj1.mass + obj2.mass);
                Vec2D velAdjustment1 = posDiff12 * massRatio1 * dot1 * (1 / pow(posDiff12.length(), 2));

                Vec2D posDiff21 = obj2.pos - obj1.pos;
                float dot2 = Vec2D::dot(obj2.vel - obj1.vel, posDiff21);
                float massRatio2 = 2.0 - massRatio1;
                Vec2D velAdjustment2 = posDiff21 * massRatio2 * dot2 * (1 / pow(posDiff21.length(), 2));

                /*
                Update velocities after computing both to avoid using new v1
                in calculation for new v2
                */
                obj1.vel = (obj1.vel - velAdjustment1) * obj1.restitutionCoeff;
                obj2.vel = (obj2.vel - velAdjustment2) * obj2.restitutionCoeff;

                /*
                Update positions by shifting each object by half the overlap
                in opposite directions along the collision axis
                */
                float overlap = obj1.radius + obj2.radius - posDiff12.length();

                Vec2D posAdjustment1 = posDiff12 * (0.5 * overlap / posDiff12.length());
                obj1.pos = obj1.pos + posAdjustment1;

                Vec2D posAdjustment2 = posDiff21 * (0.5 * overlap / posDiff21.length());
                obj2.pos = obj2.pos + posAdjustment2;
            }
        }
    }
}

void Solver::applyBounds()
{
    for (int i = 0; i < objects.size(); i++)
    {
        // collision with right wall
        if (objects[i].pos.x() + objects[i].radius > BOUNDS.right)
        {
            objects[i].pos.setX(BOUNDS.right - objects[i].radius);
            objects[i].vel.mirrorY();
            objects[i].vel = objects[i].vel * objects[i].restitutionCoeff;
        }
        // collision with left wall
        else if (objects[i].pos.x() - objects[i].radius < BOUNDS.left)
        {
            objects[i].pos.setX(BOUNDS.left + objects[i].radius);
            objects[i].vel.mirrorY();
            objects[i].vel = objects[i].vel * objects[i].restitutionCoeff;
        }
        // collision with ceiling
        if (objects[i].pos.y() + objects[i].radius > BOUNDS.up)
        {
            objects[i].pos.setY(BOUNDS.up - objects[i].radius);
            objects[i].vel.mirrorX();
            objects[i].vel = objects[i].vel * objects[i].restitutionCoeff;
        }
        // collision with floor
        else if (objects[i].pos.y() - objects[i].radius > BOUNDS.down)
        {
            objects[i].pos.setY(BOUNDS.down + objects[i].radius);
            objects[i].vel.mirrorX();
            objects[i].vel = objects[i].vel * objects[i].restitutionCoeff;
        }
    }
}

void Solver::updateObjects()
{
    for (int i = 0; i < objects.size(); i++)
    {
        objects[i].update(SUBDT);
    }
}

void Solver::addObject(Circle &obj)
{
    objects.push_back(obj);
}

void Solver::updateSolver()
{
    for (int substep = 0; substep < SUBSTEPS; substep++)
    {
        applyGravity();
        applyCollisions();
        updateObjects();
        applyBounds();
    }
    time += DT;
}

std::vector<Circle>& Solver::getObjects()
{
    return objects;
}

const RectBounds& Solver::getBounds()
{
    return BOUNDS;
}
