def run():
  bars = int(input("How many bars should be charged? "))
  i = 0
  print("")

  while i < bars:
    print("charging:", ((" 💜")*(i+1)))
    i = i + 1
  print("")
  print("The battery is now fully charged!")

