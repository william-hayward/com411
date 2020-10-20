def run():
  
  def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
  
  def menu():
    print("\nPlease select a direction:")
    direction = directions()
    for count in range(len(direction)):
      print("{}: {}".format(count, direction[count]))
    response = int(input())
    return direction[response]
  
  route = []
  print("Working out escape route...")
  for count in range(0, 5):
    route.append(menu())
  print("\nEscape route: {}".format(route))




  