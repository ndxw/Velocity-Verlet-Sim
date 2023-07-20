#include "../include/Objects.h"
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

/*
====================================================================================
OBJECT class
    - position, velocity, acceleration
    - mass
    - restitution
    - colour
====================================================================================
*/
Object::Object()
{
    
}

Object::Object(const Vec2D &pos, const Vec2D &vel, const Vec2D &acl, 
                const float mass, const float restitutionCoeff, 
                const vector<float> &colour)
{
    this->pos = pos;
    this->vel = vel;
    this->acl = acl;
    this->mass = mass;
    this->restitutionCoeff = restitutionCoeff;
    this->colour = colour;
}

Object::~Object()
{

}

void Object::update(float dt)
{
    /*
    Equations for Velocity-Verlet integration can be
    found @ https://en.wikipedia.org/wiki/Verlet_integration
    */
    
    // calculate v(t+0.5*dt)
    Vec2D half_adt = this->acl * (0.5*dt);
    Vec2D half_v = this->vel + half_adt;

    // calculate new position
    this->pos = this->pos + half_v * dt;

    // calculate new velocity
    this->vel = half_v + half_adt;

}


/*
====================================================================================
CIRCLE class, extends OBJECT
    - adds radius attribute
====================================================================================
*/
Circle::Circle()
{

}

Circle::Circle(const Vec2D &pos, const Vec2D &vel, const Vec2D &acl, 
                const float mass, const float restitutionCoeff, 
                const vector<float> &colour, const float radius)
{
    this->pos = pos;
    this->vel = vel;
    this->acl = acl;
    this->mass = mass;
    this->restitutionCoeff = restitutionCoeff;
    this->colour = colour;
    this->radius = radius;
}

Circle::~Circle()
{

}

/*
====================================================================================
RECTANGULAR BOUNDS class
    - distance of four walls to origin
====================================================================================
*/
RectBounds::RectBounds(int left = 0, int right = 1000, int up = 1000, int down = 0)
{
    this->left = left;
    this->right = right;
    this->up = up;
    this->down = down;
}

RectBounds::~RectBounds()
{

}

/*
====================================================================================
2-D VECTORS class
    - x and y components
====================================================================================
*/
Vec2D::Vec2D(float x = 0.0, float y = 0.0)
{
    xComp = x; yComp = y;
    computeLength();
}

Vec2D::~Vec2D()
{
    
}

float Vec2D::x()
{
    return xComp;
}

float Vec2D::y()
{
    return yComp;
}

void Vec2D::setX(float newX)
{
    xComp = newX; 
    computeLength();
}

void Vec2D::setY(float newY)
{
    yComp = newY; 
    computeLength();
}

float Vec2D::length()
{
    return len;
}

void Vec2D::computeLength()
{
    len = sqrt(pow(xComp, 2) + pow(yComp, 2));
}

Vec2D Vec2D::operator+(Vec2D const& addend)
{
    Vec2D sum;
    sum.xComp = xComp + addend.xComp;
    sum.yComp = yComp + addend.yComp;
    return sum;
}

Vec2D Vec2D::operator-(Vec2D const& subtrahend)
{
    Vec2D difference;
    difference.xComp = xComp - subtrahend.xComp;
    difference.yComp = yComp - subtrahend.yComp;
    return difference;
}

Vec2D Vec2D::operator*(float scalar)
{
    Vec2D scaled;
    scaled.xComp = xComp * scalar;
    scaled.yComp = yComp * scalar;
    return scaled;
}

float Vec2D::dot(Vec2D const& vec1, Vec2D const& vec2)
{
    return vec1.xComp * vec2.xComp + vec1.yComp * vec2.yComp;
}

// mirrors this vector about the x-axis
void Vec2D::mirrorX()
{
    yComp = -yComp;
}

// mirrors this vector about the y-axis
void Vec2D::mirrorY()
{
    xComp = -xComp;
}

// outputs this vector in the form (x, y)
string Vec2D::toString()
{
    ostringstream ssx, ssy;
    ssx << x;
    ssy << y;

    string output = "(" + ssx.str() + ", " + ssy.str() + ")";
    return output;
}