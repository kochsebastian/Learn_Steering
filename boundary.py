from ray import Vector
from pyprocessing import *

class Boundary:
    def __init__(self,x1,y1,x2,y2):
        self.a = Vector(x1,y1)
        self.b = Vector(x2,y2)
    
    def midpoint(self):
        return Vector((self.a.x + self.b.x) * 0.5, 
                        (self.a.y + self.b.y) * 0.5)
    
    def show(self):
        stroke(255)
        line(self.a.x, self.a.y, self.b.x, self.b.y)
    