#ifndef OBJECTS_H
#define OBJECTS_H

#include <string>
using namespace std;

class Object
{  
    public:
        Vec2D pos;
        Vec2D vel;
        Vec2D acl;
        float mass;
        float restitutionCoeff;
        vector<float> colour;

        Object();
        Object(const Vec2D &, const Vec2D &, const Vec2D &, const float, const float, const vector<float> &);
        ~Object();

        void update(float);
};

class Circle: public Object
{
    public:
        float radius;

        Circle();
        Circle(float);
        ~Circle();
}

class RectBounds
{
    private:
        int left;
        int right;
        int up;
        int down;

    public:
        RectBounds();
        RectBounds(int, int, int, int);
        ~RectBounds();

        void getBounds(vector<int> &);
}

class Vec2D
{
    private:
        float x;
        float y;
        float length;

        void computeLength();

    public:
        Vec2D(float, float);
        ~Vec2D();

        float getX();
        float getY();
        void setX(float);
        void setY(float);

        Vec2D operator+(Vec2D const&);
        Vec2D operator-(Vec2D const&);
        static float dot(Vec2D const&, Vec2D const&);
        Vec2D operator*(float);
        void mirrorX();
        void mirrorY();
        string toString();
};

#endif