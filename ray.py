import math

class Ray :
    def __init__(self,pos, angle):
        self.pos = pos
        self.angle = angle
        self.dir = Vector().from_angle(angle)

    def lookAt(self,x,y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir.normelize()

    def rotate(self,offset):
        self.dir = Vector().from_angle(self.angle + offset)

    def show(self)
        pass

    def cast(self,wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (t > 0 and t < 1 and u > 0):
            pt = Vector()
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        else
            return


class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)
    def __minus__(self, other):
        return Vector(self.x + other.x,self.y - other.y)

    def from_angle(self,a):
        self.x = math.cos(x)
        self.y = math.sin(y)
    
    def normelize(self):
        mag = math.sqrt(self.x**2+self.y**2)
        return Vector(x/mag,y/mag) 

