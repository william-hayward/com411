def display_ladder(steps):
  for i in range(steps):
    print("| |")
    print("***")
  print("| |")

def create_ladder():
  step = int(input("How many steps remain? "))
  display_ladder(step)

create_ladder()