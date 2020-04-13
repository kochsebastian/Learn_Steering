
import random
import math
from particle import Particle
# from ray import Vector





def nextGeneration(saved_particles,population,start,end,TOTAL):
    # print('new gen')
    saved_particles = calculate_fitness(saved_particles)
    population = []
    for i in range(TOTAL):
        population.append(pickOne(saved_particles,start))
    for i in range(TOTAL):
        saved_particles[i].dispose()

    saved_particles = []
    return population,saved_particles


def newGeneration(saved_particles,population,start,end,TOTAL):
    # print('new gen')
    population = []
    saved_particles = calculate_fitness(saved_particles)
    saved_particles.sort(key=lambda x: x.fitness, reverse=True)
    best80ofhalf = sorted(random.sample(range(0, math.ceil(TOTAL/2)), math.ceil(math.ceil(TOTAL/2)*1)))
    # random20ofhalf = sorted(random.sample(range(math.ceil(TOTAL/2), TOTAL), math.floor(math.ceil(TOTAL/2)*0.20)))
    index_list = sorted(best80ofhalf )
    n = TOTAL - len(index_list)
    listofzeros = [0] * n
    index_list+=listofzeros
    for i in index_list:
        particle = saved_particles[i]
        child = Particle(brain=particle.brain,start=start,max_fitness=particle.max_fitness)
        child.mutate()
        population.append(child)
    for i in range(TOTAL):
        saved_particles[i].dispose()
    saved_particles = []
    return population, saved_particles

        





def pickOne(saved_particles,start):
    # global saved_particles
    index = 0
    r  = random.random()
    while r > 0:
        r = r - saved_particles[index].fitness
        index+=1
    index-=1
    particle = saved_particles[index]
    # child = Particle(brain=particle.brain,Vector(particle.x,particle.y))
    child = Particle(brain=particle.brain,start=start,max_fitness=particle.max_fitness)
    child.mutate()
    return child




def calculate_fitness(saved_particles):
    # global saved_particles
    for particle in saved_particles:
        particle.calculate_fitness()
    
    sum_ = 0
    for particle in saved_particles:
        sum_ += particle.fitness

    for particle in saved_particles:
        particle.fitness = particle.fitness / sum_
    return saved_particles