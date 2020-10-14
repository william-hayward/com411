#ask user to enter their name
def run():
  print("What is your name human? ")
  name = input()
  print("It is nice to meet you human", name)
  print("")
  name = input("What is your name human? ")
  print("Nice to meet you human", name,".")
  print("")
  name = input("What is your name human? ")
  print("Nice to meet you human" + name + ".")
  print("")
  name = input("What is your name human? ")
  print("Nice to meet you {}.".format(name))
