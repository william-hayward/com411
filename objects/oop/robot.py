def run():

  class Robot:
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100
    def __init__(self):
      self.name = "Robot"
      self.age = 0
      self.energy = Robot.MAX_ENERGY

    def the_laws(self):
      print(Robot.laws)

    def grow(self):
      self.age += 1

    def eat(self, amount):
      if self.energy + amount > Robot.MAX_ENERGY:
        self.energy = Robot.MAX_ENERGY
      else:
        self.energy += amount

    def move(self, distance):
      if self.energy - distance < 0:
        self.energy = 0
      else:
        self.energy = self.energy - distance

    def display(self):
      print(f"I am {self.name}")

    def __repr__(self):
      return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  #if (__name__ == "main"): with the run stuff this makes it not work, on a normal program, add this line

#------------------------
  robot = Robot()

  robot.display()
  robot.the_laws()
  print(robot.__repr__())
  robot.move(30)
  robot.eat(20)
  robot.grow()
  print(robot.__repr__())