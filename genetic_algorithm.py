
import random
from particle import Particle
# from ray import Vector





def nextGeneration(saved_particles,population,start,end,TOTAL):
    print('new gen')
    calculate_fitness(end,saved_particles)
    # population = []
    for i in range(TOTAL):
        population.append(pickOne(saved_particles,start))
    for i in range(TOTAL):
        saved_particles[i].dispose()

    saved_particles = []
    return population,saved_particles





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
    child = Particle(brain=particle.brain,start=start)
    child.mutate()
    return child



def calculate_fitness(end,saved_particles):
    # global saved_particles
    for particle in saved_particles:
        particle.calculate_fitness()
    
    sum_ = 0
    for particle in saved_particles:
        sum_ += particle.fitness

    for particle in saved_particles:
        particle.fitness = particle.fitness / sum_
    return saved_particles