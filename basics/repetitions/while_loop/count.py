def run():
  live_cables = int(input("How many live cables must i avoid? "))
  i = 0 

  while i < live_cables:
    print("Avoiding.... Done!", (i+1), "live cables avoided")
    i = i + 1

  print("All live cables have been avoided!")