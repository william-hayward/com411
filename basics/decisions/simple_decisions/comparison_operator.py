def run():
  number1 = int(input("Please enter a first number "))
  number2 = int(input("Please enter a second number "))

  if number1 < number2:
    print("The first number is the smallest!")
  elif number1 > number2:
    print("The second number is the smallest!")
  else:
    print("both numbers are equal!")