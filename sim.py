
from pyprocessing import *
import random
from numpy import interp
from noise import pnoise2
from boundary import Boundary
import tensorflow as tf
from particle import Particle
from genetic_algorithm import *
from ray import Vector
import time


TOTAL = 10
generation_count = 0

walls = []
ray = None

population = []
saved_particles  = []

start = Vector()
end = Vector()

speedSlider = None

inside = []
outside = []
checkpoints = []

SIGHT = 100
LIFESPAN = 25
MUTATION_RATE = 0.1


"""
 around 5-6 successfully completed rounds will make the fitness of 500+
 so maxFitness is set to 500
 thus the changeMap will flag becomes true and we will create new map
 when any of the particle completes multiple rounds in current map
 this will help to make the current generation to work on new map
 and generalize to variety of maps
"""

max_fitness = 200
change_map = False
frame = 0


def buildTrack(n_checkpoints):
    global checkpoints
    global inside
    global outside
    global walls
    global start
    global end

    inside = []
    outside = []
    checkpoints = [] 

    noise_max = 2
    total = n_checkpoints
    pathWidth = 25
    startX = random.uniform(0,1000)
    startY = random.uniform(0,1000)
    for i in range(total):
        a = interp(i,[0,total],[0,math.pi*2])
        xoff = interp(math.cos(a),[-1,1],[0,noise_max]) + startX
        yoff = interp(math.sin(a),[-1,1],[0,noise_max]) + startY
        xr = interp(pnoise2(xoff,yoff),[0,1],[100, width*0.5])
        yr = interp(pnoise2(xoff,yoff),[0,1],[100, height*0.5])
        x1 = width / 2 + (xr - pathWidth) * math.cos(a) 
        y1 = height / 2 + (yr - pathWidth) * math.sin(a)
        x2 = width / 2 + (xr + pathWidth) * math.cos(a)
        y2 = height / 2 + (yr + pathWidth) * math.sin(a)
        checkpoints.append(Boundary(x1,y1,x2,y2))
        inside.append(Vector(x1,y1))
        outside.append(Vector(x2,y2))

    walls = []
    for i in range(len(checkpoints)):
        a1 = inside[i]
        b1 = inside[(i+1) % len(checkpoints)]
        walls.append(Boundary(a1.x,a1.y,b1.x,b1.y))
        a2 = outside[i]
        b2 = outside[(i+1) % len(checkpoints)]
        walls.append(Boundary(a2.x,a2.y,b2.x,b2.y))

    checkpoints.reverse()
    inside.reverse()
    outside.reverse()
    start = checkpoints[0].midpoint()
    end = checkpoints[len(checkpoints)-1].midpoint()

lap=0
alivetime = 0
def setup():
    global population
    global start
    global end
    global TOTAL
    global lap
    
    size(600,600)
    n_checkpoints = 100
    buildTrack(n_checkpoints)

    for i in range(TOTAL):
        population.append(Particle(start=start,max_fitness=n_checkpoints))
    frameRate(25)
    lap = time.time()
    textSize(12)
    # speedSlider = createSlider

def draw():
    global checkpoints
    global population
    global change_map
    global walls
    global generation_count
    global max_fitness
    global saved_particles
    global start
    global end
    global frame
    global lap

    global alivetime
    frame+=1


    cycles  = 1
    
    background(0)
    now = time.time() - lap


   
    fill(0)   
    noStroke()
    
    fill(255)  
    bestP = population[0]
    text ("Laptime: " + "{:.2f}".format(now) , width-150, 30)
    text ("Generation: " + str(generation_count) , width-150, 50)
    text ("Alive: " + str(len(population)) , width-150, 70)
    text ("time: " + "{:.2f}".format(alivetime) , width-150, 110)
    # print(f"alive: {len(population)}, drawtime: {draw_time}")
    
    # text ("Best: " + str(len(population)) , width-150, 50)
    
    for n in range(cycles):
        for particle in population:
          
            particle.look(walls)
            particle.check(checkpoints)
            particle.bounds()
            particle.update(LIFESPAN)
            particle.show()
            
            if particle.fitness > bestP.fitness:
                bestP = particle
  
    
        for i in range(len(population)-1,-1,-1):
            particle = population[i]
            if particle.dead or particle.finished:
                saved_particles.append(population.pop(i)) 
            
            if (not change_map) and (particle.fitness > max_fitness):
                change_map = True

        if len(population) != 0 and change_map:
            for i in range(len(population)-1,-1,-1):
                saved_particles.append(population.pop(i)) 

            # buildTrack(saved_particles[0].max_fitness) 
            population,saved_particles = nextGeneration(saved_particles,population,start,end,TOTAL)
            generation_count+=1
            lap = time.time()
            alivetime=0
    
        if len(population) == 0:
            # buildTrack(saved_particles[0].max_fitness) 
            population,saved_particles = nextGeneration(saved_particles,population,start,end,TOTAL)
            generation_count+=1
            lap = time.time()
            alivetime=0
            
    
    # for cp in checkpoints:
    #     cp.show()
    
    for wall in walls:
        wall.show()

    # for particle in population:
    #     particle.show()

    bestP.highlight(SIGHT)


    fill(255)

    noStroke()
    text ("Fitness: " + str(bestP.fitness) , width-150, 90)
    frame_name = str(frame)+".png"

    
run()