#without loop
'''def cross_bridge(distance_crossed):
  print("Crossed step.\n" * distance_crossed)
  if distance_crossed > 5:
    print("The bridge is collapsing!")
  else:
    print("We must keep going!\n")

cross_bridge(3)
cross_bridge(6)'''
  
#with loop
def cross_bridge(distance_crossed):
  for i in range(distance_crossed):
    print("Crossed step.")
  if distance_crossed > 5:
    print("The bridge is collapsing!")
  else: 
    print("We must keep going!")

cross_bridge(3)
cross_bridge(6)