class Human:
  MAX_ENERGY = 100
  def __init__(self, name="Human", age=0): 
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  def grow(self):
    self.age += 1

  def eat(self, amount):
    if self.energy + amount > Human.MAX_ENERGY:
      self.energy = Human.MAX_ENERGY
    else:
      self.energy += amount

  def move(self, distance):
    if self.energy - distance < 0:
      self.energy = 0
    else:
      self.energy = self.energy - distance

  def display(self):
    print(f"I am {self.name}")

  def __str__(self):
    return f'my name is {self.name} and i am {self.age} years old and my energy is {self.energy}.'
  
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

if (__name__ == "__main__"): 
  human = Human()
  
  human.display()
  print(human.__str__())
  human.move(30)
  human.eat(20)
  human.grow()
  print(human.__str__())
