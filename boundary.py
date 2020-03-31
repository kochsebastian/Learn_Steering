from ray import Vector

class Boundary:
    def __init__(self,x1,y1,x2,y2):
        self.a = Vector(x1,y1)
        self.b = Vector(x2,y2)
    
    def midpoint(self):
        return Vector((self.a.x + self.b.x) * 0.5, 
                        (self.a.y + self.b.y) * 0.5)
    
    def show(self):
        pass

    