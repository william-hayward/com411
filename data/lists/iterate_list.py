def run():
  def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

  def menu():
    print("Please select a direction:")
    direction = directions()
    for count in range(len(direction)):
      print("{}: {}".format(count, direction[count]))
  menu()