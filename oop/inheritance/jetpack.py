from tech import Tech
class Jetpack(Tech):
  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "Jetpack()"

  def activate():
    print("Jetpack has been activated")
  
  def deactivate():
    print("Jetpack has been deactivated")

if (__name__ == "__main__"):
  jetpack = Jetpack()
  print(jetpack.__repr__())