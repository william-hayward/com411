import random

def guess_the_number():
  minimum = int(input("Please enter the minimum value:\n"))
  maximum = int(input("\nPlease enter the maximum value:\n"))
  number_to_guess = random.randrange(minimum, maximum)

  print("\nI am thinking of a number between {} and {}. Can you guess what it is?\n".format(minimum, maximum))

  guessed = False
  tries = 0

  while guessed != True:
    guess = int(input("Your guess:\n"))
    if guess == number_to_guess:
      tries = tries + 1
      print("\nWell done! you guessed the number! It was: {}".format(number_to_guess)) 
      print("Tries: {}\n".format(tries))
      guessed = True
    elif guess < number_to_guess:
      tries = tries + 1
      print("\nYour guess is too low! Try again")
      print("Tries: {}\n".format(tries))
    elif guess > number_to_guess:
      tries = tries + 1
      print("\nYour guess is too high! Try again")
      print("Tries: {}\n".format(tries))

guess_the_number()

