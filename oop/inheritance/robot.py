from inhabitant import Inhabitant

class Robot(Inhabitant):
  laws = "Protect, Obey and Survive"
  def __init__(self, name = "Robot", age = 0, energy = 100):
    super().__init__(name, age, energy)
  
  def __str__(self):
    return f'My name is {self.name}, I am {self.age} years old and i my energy is {self.energy}'
  
  def __repr__(self):
    return f'Robot(name = {self.name}, age = {self.age}, energy = {self.energy})'
  
  def display(self):
    print(f'I am {self.name}')
  
  def the_laws(self):
    print(Robot.laws)

if (__name__ == "__main__"):
  robot = Robot("Beep", 0)
  print(robot.__repr__())
  robot.move(40)
  robot.eat(25)
  robot.grow()
  print(robot.__repr__())