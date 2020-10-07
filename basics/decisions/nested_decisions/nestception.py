found = False
while found == False:
  location = input("Where should i look? ")

  if location == "in the bedroom":
    bedroom_location = input("Where in the bedroom should i look? ")
    if bedroom_location == "under the bed":
      print("I found some shoes but theres no battery!")
    else:
      print("I found some mess but theres no battery!")
  elif location == "in the bathroom":
    bathroom_location = input("Where in the bathroom should i look? ")
    if bathroom_location == "in the bathtub":
      print("I found a rubber duck but theres no battery!")
    else:
      print("I found a wet surface but theres no battery!")
  elif location == "in the lab":
    lab_location = input("Where in the lab should i look? ")
    if lab_location == "on the table":
      print("YES! I found the battery!")
      found = True
    else:
      print("I found some tools but theres no battery!")
  else:
    print("I do not know where that is but i will keep looking!")