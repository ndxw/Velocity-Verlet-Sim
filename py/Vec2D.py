from math import sqrt

class Vec2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.mag = sqrt(x**2 + y**2)

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
    def dot(*vecs):
        product_x, product_y = 1, 1
        for vec in vecs:
            product_x *= vec.x
            product_y *= vec.y
        return product_x + product_y

    @staticmethod
    def scale(vec1, scalar = 1.0):
        vec3_x = vec1.x * scalar
        vec3_y = vec1.y * scalar
        return Vec2D(vec3_x, vec3_y)
    
    # mirrors vector about x-axis
    def mirror_x(self):
        self.y *= -1.0

    # mirrors vector about y-axis
    def mirror_y(self):
        self.x *= -1.0
    
    def to_string(self):
        return f'({self.x}, {self.y})'