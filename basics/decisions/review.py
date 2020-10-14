def run():
  lives = int(input("Please enter the number of lives "))
  energy = int(input("Please enter the energy level "))
  shield = int(input("Please enter the shield level "))
  eyes = input("enter the character that will be displayed as the robot's eyes ")
  name = input("What is your name? ")

  lives_symbol = " 💚"
  energy_symbol = " 💛"
  shield_symbol = " 💗"

  print("")
  print("Setting health....\n")
  print("Lives:  ", (lives_symbol*lives))
  print("Energy: ", (energy_symbol*energy))
  print("Shield: ", (shield_symbol*shield))
  print("")
  print("setting robot...\n")

  print("   ########")
  print("   #",eyes,"",eyes,"#")
  print("   # ---- #      Hello",name+"! I am Beep! A robot!")
  print("   ########")
  print("##############")
  print("#  #      #  #")
  print("#  #      #  #")
  print("#  #      #  #")
  print("##############")
  print("   ########")
  print("   #  ##  #")
  print("   #  ##  #")
  print("   #  ##  #")
  print("   ########\n\n")

  games = input("Do you like games? (y/n) ")
  if games == "y":
    decision = input("Would you like to play a game now? (y/n) ")
    if decision == "y":
      print("yay!, lets play a counter game!")
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

    elif decision == "n":
      print("Aw! maybe some other time..")
    else:
      print("Please enter a valid answer!")

  elif games == "n":
    books = input("aw! thats a shame, do you like books then? (y/n) ")
    if books == "y":
      fav = input("Whats your favourite genre? ")
      length = input("Also, do you prefer short or long books? ")
      if fav == "sci-fi" and length == "long":
        print("OMG me too! i like sci-fi books and especially long ones!")
      else:
        print("thats awesome! ill have to read something like that!")
    elif books == "n":
      print("awwww.. that sucks")
    else:
      print("enter a valid answer!")
  else:
    print("enter a valid answer!")

