#ifndef SOLVER_H
#define SOLVER_H

#include "Objects.h"

class Solver
{
    private:
        float time;
        vector<Object> objects;
        const Vec2D GRAVITY;
        const RectBounds BOUNDS;
        const int FRAMERATE, SUBSTEPS, MAX_OBJECTS;
        const float DT, SUBDT;

        void applyGravity();
        void applyCollisions();
        void applyBounds();
        void updateObjects();
        
    public:
        Solver();
        ~Solver();

        void addObject(Object &);
        void updateSolver();

        vector<Object>& getObjects();
        RectBounds& getBounds();
}

#endif