import random
from human import Human
from robot import Robot
from planet import Planet

class Universe:
  def __init__(self):
    self.planets = []

  def generate(self):
    planet = Planet()
    for count in range(random.randint(0 ,10)):
      robot = Robot(f"Robot{count}")
      planet.add_robot(robot) 

    for count in range(random.randint(0 ,10)):
      human = Human(f"Human{count}")
      planet.add_human(human) 

    self.planets.append(planet)

  def __repr__(self):
    return f"universe(planets={self.planets})"
  def __str__(self):
    return f"The universe contains {len(self.planets)} planets"

if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  print(universe.__repr__())
  print("")
  print(universe.__str__())