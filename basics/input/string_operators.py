lives = int(input("Please enter the number of lives "))
energy = int(input("Please enter the energy level "))
shield = int(input("Please enter the shield level "))

lives_symbol = " 💚"
energy_symbol = " 💛"
shield_symbol = " 💗"

print("")
print("Setting health....\n")
print("Lives:  ", (lives_symbol*lives))
print("Energy: ", (energy_symbol*energy))
print("Shield: ", (shield_symbol*shield))

