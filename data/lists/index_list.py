def run():
  def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

  print("Moving...")
  direction = movements()
  for count in range(0, 7, 2):
    print("{} for {} steps".format(direction[count], direction[count + 1]))
    
  