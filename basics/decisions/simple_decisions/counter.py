def run():
  number1 = int(input("Please enter a first number "))
  number2 = int(input("Please enter a second number "))
  number3 = int(input("Please enter a third number "))

  even = 0
  odd = 0 

  if (number1 % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1

  if (number2 % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1

  if (number3 % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1

  print("There are {} even numbers and {} odd numbers".format(even, odd))
