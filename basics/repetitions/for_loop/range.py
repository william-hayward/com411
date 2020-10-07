'''even = False

while even == False:
  brightness = int(input("What level of brightness is required? (even number) "))
  if (brightness % 2) == 0:
    even = True
    print("Adjusting brightness...\n")
    for i in range(2, brightness + 1, 2):
      print("Beep's brightness level:","*"*i)
      print("Bop's brightness level:","*"*i)
      print("")
    print("\nAdjustments complete!")
    

  else:
    print("Please enter an even number")'''

brightness = int(input("What level of brightness is required? "))
print("\nAdjusting brightness...\n")
for i in range(2, brightness + 1, 2):
      print("Beep's brightness level:","*"*i)
      print("Bop's brightness level:","*"*i)
      print("")
print("\nAdjustments complete!")