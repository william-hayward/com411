phrase = input("What phrase do you see? ")
print("\nReversing...\n")
print("The phrase is: ",end="")

for i in range(len(phrase)-1, -1, -1):
  print(phrase[i], end="")
