from tech import Tech

class Laser(Tech):
  MAX_RANGE = 100
  def __init__(self):
    super().__init__()
  
  def __repr__(self):
    return f"laser()"
  
  def activate():
    print("Laser has been activated")
  
  def deactivate():
    print("Laser has been deactivated")
  
  def fire(distance):
    if distance > Laser.MAX_RANGE:
      print(f"Fire maximum range of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {Laser.MAX_RANGE}")

if (__name__ == "__main__"):
  laser = Laser()
  print(laser.__repr__())
