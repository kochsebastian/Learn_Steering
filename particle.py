
from ray import Ray
import math
from ray import Vector
from numpy import interp

from nn import NeuralNetwork
from pyprocessing import * 
# import env 




def p1distance(p1,p2,x,y):
    num = abs((p2.y-p1.y)*x 
            - (p2.x-p1.x)*y
            + p2.x * p1.y
            - p2.y * p1.x 
            )
    # den = 
    den = p1.dist(p2)
    return num / den

class Particle:
    def __init__(self,brain=False,start=Vector(),SIGHT=50):
        self.fitness = 0 
        self.dead = False 
        self.finished = False 
        self.pos = Vector(start.x, start.y) 
        self.vel = Vector() 
        self.acc = Vector() 
        self.maxspeed = 5 
        self.maxforce = 0.2 
        self.sight = SIGHT 
        self.rays = [] 
        self.index = 0 
        self.counter = 0 

        for a in range(-45,45,15):
            self.rays.append(Ray(self.pos,math.radians(a)))
        
        if brain:
            self.brain = brain.copy()
        else:
            self.brain = NeuralNetwork(len(self.rays), (len(self.rays) * 2), 2)

    def dispose(self):
        #  pass
        self.brain.dispose()
    

    def mutate(self,MUTATION_RATE=0.1):
        # global MUTATION_RATE
        self.brain.mutate(MUTATION_RATE) # TODO mutation rate
    
    def apply_force(self,force):
        self.acc += force


    def update(self,LIFESPAN):
        if not self.dead and not self.finished:
            self.pos += self.vel
            self.vel += self.acc
            self.vel.limit(self.maxspeed)
            self.acc.x=0
            self.acc.y=0
            self.counter+=1
            if self.counter > LIFESPAN: #TODO lifespan
                self.dead = True
            
            for i in range(len(self.rays)):
                self.rays[i].rotate(self.vel.heading())


    def check(self,checkpoints):
        if not self.finished:
            self.goal = checkpoints[self.index]
            d = p1distance(self.goal.a, self.goal.b, self.pos.x,self.pos.y)
            if d < 5:
                self.index = (self.index + 1) % len(checkpoints)
                self.fitness+=1
                self.counter = 1

    def calculate_fitness(self):
        self.fitness = math.pow(2,self.fitness)

    def look(self, walls):
        inputs = []
        for i in range(len(self.rays)):
            ray = self.rays[i]
            closest = None
            record = self.sight
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = self.pos.dist(pt)
                    if d < record and d < self.sight:
                        record = d 
                        closest = pt
            if record < 5:
                self.dead = True
        
            inputs.append(interp(record, [0, 50], [1, 0]))

            if closest:
                pass

        output = self.brain.predict(inputs) 
        angle = interp(output[0],[0,1],[-math.pi, math.pi])
        speed = interp(output[1], [0, 1], [0, self.maxspeed])
        angle += self.vel.heading()
        steering = Vector().from_angle(angle)
        steering.set_mag(speed)
        steering -= self.vel
        steering.limit(self.maxforce)
        self.apply_force(steering)

    def bounds(self):
        if self.pos.x > width or self.pos.x < 0 or self.pos.y > height or self.pos.y < 0:
            self.dead = True

    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        heading = self.vel.heading()
        rotate(heading)
        fill(255,100)
        rectMode(CENTER)
        rect(0,0,10,5)
        popMatrix()

    def highlight(self,SIGHT):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        heading = self.vel.heading()
        rotate(heading)
        stroke(0, 255, 0)
        fill(0, 255, 0)
        rectMode(CENTER)
        rect(0, 0, 20, 10)
        popMatrix()
        for ray in self.rays:
            ray.show(self,SIGHT)
        
        if self.goal:
            self.goal.show()
        