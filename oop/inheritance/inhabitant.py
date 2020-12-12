from abc import ABC
class Inhabitant(ABC):
  MAX_ENERGY = 100
  def __init__(self, name="Inhabitant", age = 0, energy = MAX_ENERGY):
    self.age = age
    self.energy = energy
    self.name = name

  def grow(self):
    self.age += 1
  
  def eat(self, amount):
    if self.energy + amount > Inhabitant.MAX_ENERGY:
      self.energy = Inhabitant.MAX_ENERGY
    else:
      self.energy += amount
    
  def move(self, distance):
    if self.energy - distance < 0:
      self.energy = 0
    else:
      self.energy = self.energy - distance
  
