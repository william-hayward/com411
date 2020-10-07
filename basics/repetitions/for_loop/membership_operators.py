phrase = input("What phrase do you see? ")
print("\nReversing...\n")
print("The phrase is: ",end="")

reversed = ""
for i in phrase:
  reversed = i + reversed
print(reversed)