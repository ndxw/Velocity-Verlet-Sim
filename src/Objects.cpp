#include "Objects.h"
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
                const float mass, const float restitutionCoeff, const vector<float> &colour);
{
    this.pos = pos;
    this.vel = vel;
    this.acl = acl;
    this.mass = mass;
    this.restitutionCoeff = restitutionCoeff;
    this.colour = colour;
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
    vector<float> half_adt = this.acl * (0.5*dt);
    vector<float> half_v = this.vel + half_adt;

    // calculate new position
    this.pos = this.pos + half_v * dt;

    // calculate new velocity
    this.vel = half_v + half_adt;

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

Circle::Circle(float radius)
{

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
RectBounds::RectBounds(int left = 0, int right = 0, int up = 1000, int down = 1000)
{
    this.left = left;
    this.right = right;
    this.up = up;
    this.down = down;
}

RectBounds::~RectBounds()
{

}

void RectBounds::getBounds(vector<int> &bounds)
{
    bounds.clear(); bounds.reserve(4); bounds.resize(4); bounds.shrink_to_fit();
    bounds[0] = left;
    bounds[1] = right;
    bounds[2] = up;
    bounds[3] = down;
}

/*
====================================================================================
2-D VECTORS class
    - x and y components
====================================================================================
*/
Vec2D::Vec2D(float x = 0.0, float y = 0.0)
{
    this.x = x; this.y = y;
    computeLength();
}

Vec2D::~Vec2D()
{
    
}

float Vec2D::getX()
{
    return x;
}

float Vec2D::getY()
{
    return y;
}

void Vec2D::setX(float newX)
{
    x = newX; 
    computeLength();
}

void Vec2D::setY(float newY)
{
    y = newY; 
    computeLength();
}

void Vec2D::computeLength()
{
    length = sqrt(pow(x, 2) + pow(y, 2));
}

Vec2D Vec2D::operator+(Vec2D const& addend)
{
    Vec2D sum;
    sum.x = x + addend.x;
    sum.y = y + addend.y;
    return sum;
}

Vec2D Vec2D::operator-(Vec2D const& subtrahend)
{
    Vec2D difference;
    difference.x = x - subtrahend.x;
    difference.y = y - subtrahend.y;
    return difference;
}

Vec2D Vec2D::operator*(float scalar)
{
    Vec2D scaled;
    scaled.x = x * scalar;
    scaled.y = y * scalar;
    return scaled;
}

static float Vec2D::dot(Vec2D const& vec1, Vec2D const& vec2)
{
    return vec1.x * vec2.x + vec1.y * vec2.y;
}

// mirrors this vector about the x-axis
void Vec2D::mirrorX()
{
    y = -y;
}

// mirrors this vector about the y-axis
void Vec2D::mirrorY()
{
    x = -x;
}

// outputs this vector in the form (x, y)
string Vec2D::toString()
{
    ostringstream ssx, ssy;
    ssx << x;
    ssy << y;

    string output = "(" + ssx.str() + ", " + ssy.str() + ")"
    return output;
}