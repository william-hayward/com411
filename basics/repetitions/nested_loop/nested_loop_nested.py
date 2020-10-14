def run():
  columns = int(input("How many columns should i have? "))
  rows = int(input("How many rows should i have? "))
  emoji = ":-)"

  for i in range(0, columns,1):
    for i in range(0, rows, 1):
      print(emoji, end="")
    print()
  print("\nDone!")