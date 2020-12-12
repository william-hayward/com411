from inhabitant import Inhabitant

class Human(Inhabitant):
  def __init__(self, name = "Human", age = 0, energy = 100):
    super().__init__(name, age, energy)
  
  def __str__(self):
    return f'my name is {self.name} and i am {self.age} years old and my energy is {self.energy}.'
  
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human("Will", 19)
  print(human.__str__())
  human.move(30)
  human.eat(20)
  human.grow()
  print(human.__str__())

