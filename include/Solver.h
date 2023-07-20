#ifndef SOLVER_H
#define SOLVER_H

#include "./Objects.h"

class Solver
{
    private:
        float time;
        std::vector<Circle> objects;
        const Vec2D GRAVITY = Vec2D(0.0, -3000.0);
        const RectBounds BOUNDS = RectBounds(0, 1000, 1000, 0);
        const int FRAMERATE = 60;
        const int SUBSTEPS = 2;
        const int MAX_OBJECTS = 10;
        const float DT = 1 / FRAMERATE;
        const float SUBDT = DT / SUBSTEPS;

        void applyGravity();
        void applyCollisions();
        void applyBounds();
        void updateObjects();
        
    public:
        Solver();
        ~Solver();

        void addObject(Circle &);
        void updateSolver();

        std::vector<Circle>& getObjects();
        const RectBounds& getBounds();
};

#endif