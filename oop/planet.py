from human import Human
from robot import Robot

class Planet:
  def __init__(self):
    self.humans = []
    self.robots = []
    
  def add_human(self, human):
    self.humans.append(human)

  def add_robot(self, robot):
    self.robots.append(robot)

  def remove_human(self, human):
    self.humans.remove(human)

  def remove_robot(self, robot):
    self.robots.remove(robot)

  def __str__(self):
    return f'This planet has {len(self.humans)} humans and {len(self.robots)} robots'

  def __repr__(self):
    return f'planet(humans={self.humans}, robots={self.robots})'


if (__name__ == "__main__"):
#------------------------
  planet = Planet()
  
  print(planet.__repr__())
  print(planet.__str__())

#------------------------
  Will = Human("Will")
  planet.add_human(Will)

#------------------------
  Beep = Robot("Beep")
  planet.add_robot(Beep)

#------------------------
  print(planet.__repr__())
  print(planet.__str__())