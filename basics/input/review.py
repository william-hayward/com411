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
print("   ########")
