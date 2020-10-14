def run():
  number = int(input("Please enter a whole number "))

  calculated_number = (number % 2)

  if calculated_number == 0:
    print(number, "is an even number!")
  else:
    print(number, "is an odd number!")