import random
import matplotlib.pyplot as plt
import numpy as np
from human import Human
from robot import Robot
from planet import Planet

class Universe:
  def __init__(self):
    self.planets = []
    self.humans = 0
    self.robots = 0

  def generate(self):
    planet = Planet()
    for count in range(random.randint(0, 100)):
      robot = Robot(f"Robot{count}")
      planet.add_robot(robot)
      self.robots = self.robots + 1 

    for count in range(random.randint(0, 100)):
      human = Human(f"Human{count}")
      planet.add_human(human)
      self.humans = self.humans + 1 

    self.planets.append(planet)
    
  
  def show_populations(self):
    subplots_num = len(self.planets)

    fig, axs = plt.subplots(1, subplots_num, sharey = "all")
    
    plt.suptitle("Population of Humans vs Robots Per Planet")

    for count in range(subplots_num):
      planet = self.planets[count]
      humans_num = len(planet.inhabitants['humans'])
      robots_num = len(planet.inhabitants['robots'])
      axs[0].set_ylabel("Population")
      axs[count].set_xlabel(f"Planet {count+1}")
      axs[count].set_yticks([])
      axs[count].set_xticks([])
      axs[0].set_yticks([0, 20, 40, 60, 80, 100])
      axs[count].bar([1,2], [humans_num, robots_num])
    
    
    plt.tight_layout
    plt.show()

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets,{self.humans} humans and {self.robots} robots"

if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.generate()
  universe.generate()
  universe.generate()
  universe.generate()
  #print(universe.__repr__())
  print("")
  print(universe.__str__())
  print("")
  universe.show_populations()
  