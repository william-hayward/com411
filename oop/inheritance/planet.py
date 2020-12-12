from human import Human 
from robot import Robot 

class Planet:
  def __init__(self):
    self.inhabitants = []
  
  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants."
  
  def __repr__(self):
    return f"Planet(inhabitants = {self.inhabitants})"
  
  def add_inhabitant(self, inhabitant):
    self.inhabitants.append(inhabitant)
  
  def remove_inhabitant(self, inhabitant):
    self.inhabitants.remove(inhabitant)
  
if (__name__ == "__main__"):
  planet = Planet()
  print(planet.__str__())
  Will = Human("Will", 19)
  planet.add_inhabitant(Will)
  print(planet.__repr__())
  print(planet.__str__())
  