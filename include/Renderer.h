#ifndef RENDERER_H
#define RENDERER_H

#include "Solver.h"

class Renderer
{
    private:
        static int RESOLUTION;

    public:
        static void render(Solver &);
}

#endif