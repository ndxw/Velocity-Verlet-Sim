#ifndef OBJECTS_H
#define OBJECTS_H

#include <string>
#include <vector>

class Vec2D
{
    private:
        float xComp;
        float yComp;
        float len;

        void computeLength();

    public:
        Vec2D(float, float);
        ~Vec2D();

        float x();
        float y();
        void setX(float);
        void setY(float);
        float length();

        Vec2D operator+(Vec2D const&);
        Vec2D operator-(Vec2D const&);
        static float dot(Vec2D const&, Vec2D const&);
        Vec2D operator*(float);
        void mirrorX();
        void mirrorY();
        std::string toString();
};

class Object
{  
    public:
        Vec2D pos;
        Vec2D vel;
        Vec2D acl;
        float mass;
        float restitutionCoeff;
        std::vector<float> colour;

        Object();
        Object(const Vec2D &, const Vec2D &, const Vec2D &, 
                const float, const float, const std::vector<float> &);

        void update(float);
};

class Circle: public Object
{
    public:
        float radius;

        Circle();
        Circle(const Vec2D &, const Vec2D &, const Vec2D &, 
                const float, const float, const std::vector<float> &, const float);
        ~Circle();
};

class RectBounds
{
    public:
        int left;
        int right;
        int up;
        int down;

        RectBounds(int, int, int, int);
        ~RectBounds();
};

#endif