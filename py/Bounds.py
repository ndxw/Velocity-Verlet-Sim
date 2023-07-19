

'''
Bounds.render() takes colour argument in the form of
3-element tuple, each element being the normalized forms of
the red, green, and blue channels
    e.g.    white -> (1.0, 1.0, 1.0)
            red   -> (1.0, 0.0, 0.0)
            teal  -> (0.15, 0.77, 0.85)
'''

class RectBounds:

    def __init__(self, left = 0, right = 1000, up = 1000, down = 0):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def render(self, colour):
        pass

class CircleBounds:
    
    def __init__(self, radius = 500):
        self.radius = radius

    def render(self, colour):
        pass