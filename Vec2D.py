from math import sqrt

class Vec2D:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.mag = float(sqrt(x**2 + y**2))

    @staticmethod
    def add(*vecs):
        vec3_x, vec3_y = 0, 0
        
        for vec in vecs:
            vec3_x += vec.x
            vec3_y += vec.y
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

if __name__ == "__main__":
    vec1 = Vec2D(1.0, 2.0)
    vec2 = Vec2D(3.0, 4.5)
    vec3 = Vec2D(-2.5, -7.0)

    sum1 = Vec2D.add(vec1, vec2)
    sum2 = Vec2D.add(vec1, vec2, vec3)

    print(sum1.x, sum1.y)
    print(sum2.x, sum2.y)