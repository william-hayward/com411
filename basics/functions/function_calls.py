def run():
  word = input("Please enter a word:\n")

  print("\nPlease choose one of the following options:")
  print("[1] Display in a box")
  print("[2] Display lower-case")
  print("[3] Display upper-case")
  print("[4] Display mirrored")
  print("[5] Display repeated")
  print("[6] Quit")
  option = int(input())

  if option == 1:
    displaybox(word)
  elif option == 2:
    lower_case(word)
  elif option == 3:
    upper_case(word)
  elif option == 4:
    mirrored(word)
  elif option == 5:
    repeated(word)
  elif option == 6:
    print("\nProgram quitted.")
  else:
    print("\nPlease enter a valid answer.")

def displaybox(word):
 dashes = 4 + len(word)
 print("")
 print("-" * dashes)
 print("| {} |".format(word))
 print("-" * dashes) 

def lower_case(word):
  print("")
  print(word.lower())

def upper_case(word):
  print("")
  print(word.upper())

def mirrored(word):
  print("")
  mirrored = ""
  for i in reversed(word):
    mirrored += i
  print("{} | {}".format(word, mirrored))
  #another way to reverse a word
  #for i in range(len(word)-1, -1, -1):
    #print(word[i], end="")

def repeated(word):
  response = int(input("\nHow many times do you want to display the word? \n"))
  print("")
  for i in range(0, response):
    if i % 2 == 0:
      print(word.lower())
    else:
      print(word.upper())
  