distance = int(input("How many steps away are we from the cave? "))

for i in range(distance):
  print((distance-i),"steps are remaining")

print("We have reached the cave!")

#alternative way from what i did:
'''for i in range(distance, 0, -1): 
  #distance, start of sequence. 0, stop value of sequence
  # -1, the step (diff of each number in sequence)
    print(i, "steps remaining")

print("We have reached the cave!")'''
  