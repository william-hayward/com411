from human import Human
from robot import Robot

class Planet:
  def __init__(self):
    self.inhabitants = {
      'humans':[],
      'robots':[]
    }
    
    
  def add_human(self, human):
    self.inhabitants['humans'].append(human)

  def add_robot(self, robot):
    self.inhabitants['robots'].append(robot)

  def remove_human(self, human):
    self.inhabitants['humans'].remove(human)

  def remove_robot(self, robot):
    self.inhabitants['robots'].remove(robot)

  def __str__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots"

  def __repr__(self):
    return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"


if (__name__ == "__main__"):
#------------------------
  planet = Planet()
  human = Human()
  robot = Robot()
#------------------------
  print(planet.__repr__())
  print(planet.__str__())
#------------------------
  Will = Human("Will", 19)
  Will.move(30)
  planet.add_human(Will)

  Libby = Human("Libby", 11)
  Libby.move(10)
  Libby.eat(5)
  planet.add_human(Libby)
#------------------------
  Beep = Robot("Beep")
  Beep.move(60)
  Beep.eat(25)
  planet.add_robot(Beep) 
#------------------------
  print("")
  print(planet.__repr__())
  print(planet.__str__())