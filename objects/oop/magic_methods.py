def run():
  class Robot:
    laws = "Protect, Obey and Survive"
    def __init__(self):
      self.name = "Robot"
      self.age = 0
    def the_laws(self):
      print(Robot.laws)
    def display(self):
      print(f"I am {self.name}")
    def __repr__(self):
      return f'robot(name={self.name}, age{self.age})'

  class Human:
    def __init__(self):
      MAX_ENERGY = 100 
      self.name = "Human"
      self.age = 0
      self.energy = MAX_ENERGY
    def display(self):
      print(f"I am {self.name} and my age is {self.age}")
    def __str__(self):
      return f'my name is {self.name} and i am {self.age} years old.'


  #if (__name__ == "main"): with the run stuff this makes it not work, on a normal program, add this line
  robot = Robot()
  robot.display()
  robot.the_laws()
  human = Human()
  human.display()
  print(robot.__repr__())
  print(human.__str__())
