def run():
  number = int(input("Please enter a number: "))
  i = 0
  answer = 1

  while i < number:
    i = i + 1
    answer = answer * i

  print("The factorial is", answer)