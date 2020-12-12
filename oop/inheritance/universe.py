from human import Human
from robot import Robot
from planet import Planet
import random
import matplotlib.pyplot as plt

class Universe:
  def __init__(self):
    self.planets = []
    
  def __repr__(self):
    return f"Universe(planets={self.planets})"
  
  def generate(self):
    planet = Planet()
    for count in range(random.randint(0, 10)):
      robot = Robot(f"Robot{count}")
      planet.add_inhabitant(robot)
    for count in range(random.randint(0, 10)):
      human = Human(f"Human{count}")
      planet.add_inhabitant(human)
    self.planets.append(planet)

  def show_population(self):
    num_subplots = len(self.planets)
    fig = plt.figure()
    
    for count in range(num_subplots):
      planet = self.planets[count]
      num_humans = 0
      num_robots = 0
      for inhabitants in planet.inhabitants:
        if isinstance(inhabitants, Human):
          num_humans += 1
        elif isinstance(inhabitants, Robot):
          num_robots += 1 
      
      ax = fig.add_subplot(1, num_subplots, count + 1)
      ax.bar([1, 2], [num_humans, num_robots])
    plt.tight_layout()
    plt.show()

if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.generate()
  universe.generate()
  universe.show_population()