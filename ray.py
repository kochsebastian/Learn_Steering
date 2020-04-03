import math
from pyprocessing import *
# import env



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

    def show(self,particle,SIGHT):
        stroke(0, 255, 0, 100)
        # pushMatrix()
        # translate(self.pos.x, self.pos.y)
        line(particle.pos.x, particle.pos.y, particle.pos.x + self.dir.x * SIGHT, particle.pos.y+self.dir.y * SIGHT)
        # pushMatrix()

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
        else:
            return


class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    
    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x,self.y - other.y)

    def __mul__(self,other):
        if isinstance(other,type(Vector())):
            return Vector(self.x*other.x,self.y*other.y) # assume dot product
        else:
            return Vector(self.x *other, self.y * other)
        return Vector(self.x)

    def __truediv__(self,other):
        if isinstance(other,Vector()):
            return Vector(self.x/other.x,self.y/other.y) # assume dot product
        else:
            return Vector(self.x /other, self.y / other)
        return Vector(self.x)

    def from_angle(self,a):
        self.x = math.cos(a)
        self.y = math.sin(a)
        return Vector(self.x,self.y)
    
    def normelize(self):
        mag = math.sqrt(self.x**2+self.y**2)
        if mag == 0:
            return Vector(0,0)
        else:
            return Vector(self.x/mag,self.y/mag) 
    
    def limit(self,limit):
        mag = math.sqrt(self.x**2+self.y**2)
        if mag == 0:
            return Vector(0,0)

        else:
            scale = limit/mag
            return Vector(self.x*scale,self.y*scale)

    def heading(self): # TODO angle range
        normelized = self.normelize()
        return math.atan2(self.y,self.x)


    def dist(self, other):
        return math.sqrt( (self.x - other.x)**2
                        + (self.y - other.y)**2
                        )
    
    def set_mag(self,mag):
        return self.normelize() * mag



