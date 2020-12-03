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
    for count in range(random.randint(0, 10)):
      robot = Robot(f"Robot{count}")
      planet.add_robot(robot)
      self.robots = self.robots + 1 

    for count in range(random.randint(0, 10)):
      human = Human(f"Human{count}")
      planet.add_human(human)
      self.humans = self.humans + 1 

    self.planets.append(planet)
  
  def show_populations(self):
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey = "all")
    
    plt.suptitle("Population of Humans and Robots In A Planet")

    ax1.set_xlim(0, 2)
    ax1.set_ylim(0, 15)
    ax1.set_xlabel("Humans")
    ax1.set_ylabel("Population")
    ax1.set_xticks([])

    #len of humans in dict for y value - cant get it to retrieve the length of the dict
    ax1.bar(1, self.humans)

    ax2.set_xlim(0, 2)
    ax2.set_ylim(0, 15)
    ax2.set_xlabel("Robots")
    ax2.set_xticks([])

    #len of robots in dict for y value - cant get it to retrieve the length of the dict
    ax2.bar(1, self.robots)

    plt.tight_layout
    plt.show()

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets, {self.robots} robots and {self.humans} humans"

if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  print(universe.__repr__())
  print("")
  print(universe.__str__())
  print("")
  universe.show_populations()
  