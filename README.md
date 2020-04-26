# Learn_Steering
The problem here is for an agent to complete a randomly generated round course without bumping into the track limits (possibly as fast as possible). This problem can be solved in many ways. An interesting approch is geneetic algorithms. 

## Genetic Algorithm
Genetic Alorithms are inspired by biology. Instead of implementing an agent that can do a predefined task as instructed, a whole generation of agents with a random behavior will be implemented. Over multiple generations concepts of mutation (random change in the behavior) and natural selections (chosing the best agents) will result in a group of agents that can solve the given task without being specially instructed to do so. A measure on how well the agents can solve the given task a fitness function is used that evaluates how well an agent is solving the task.

## Implementation
Every agent has a brain which processes the environment of the agent and based on that decides what the best action would be to reach the goal. The brain is implemented here as a very small neural network that has 7 inputs which sense the environment in different directions. The input layer is followed by a hidden layer with double the nodes of the input layer. The hidden layer is followed by the output layer which has two nodes. The first output node represents the desired speed, whereas the second node represents the deesired steering angle.

At the start of the simulation a generation of agents is created with random brains. The fitness of an agent rises when an agent reaches a new checkpoint of the course. Has an agent not reached a checkpoint in a certain time the agent will die. Has an agend reached the goal the agent will be awarded extra fitness for reaching the goal, after that the agent dies too.
An episode is completed when every agent in the generation has died. In a process of natural selection the next generation is created from the old generation. The higher the fitness of an agent the more likely it is that the agend passes it's brain to the next generation. But with a certain randomness poor performing agents cann pass their brain to the next generation to. Random mutations of the brain can happen when passing the brain to the next generation. The new generation has the same size as the generation before and every agent will try to reach the goal again.

## Results
Single Map | Random Map
--- | --- 
![Animation](resources/cars_single_speed.gif) | ![Animation](resources/cars_random.gif) | 


