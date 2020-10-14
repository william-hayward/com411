def run():
  adventure = input("What type of adventure should i have? ")

  if adventure == "short" or adventure == "scary":
    print("Im entering the dark forest!")
  elif adventure == "safe" or adventure == "long":
    print("Im taking the safe route!")
  else:
    print("Im not sure which route to take..")

  