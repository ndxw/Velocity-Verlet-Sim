from math import sqrt

class Vec2D:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.mag = float(sqrt(x**2 + y**2))

    @staticmethod
    def add(vec1, vec2):
        vec3_x = vec1.x + vec2.x
        vec3_y = vec1.y + vec2.y
        return Vec2D(vec3_x, vec3_y)
    
    @staticmethod
    def subtract(vec1, vec2):
        vec3_x = vec1.x - vec2.x
        vec3_y = vec1.y - vec2.y
        return Vec2D(vec3_x, vec3_y)
    
    @staticmethod
    def scale(vec1, scalar = 1.0):
        vec3_x = vec1.x * scalar
        vec3_y = vec1.y * scalar
        return Vec2D(vec3_x, vec3_y)
    
    def print(self):
        print(f'({self.x}, {self.y})')