def run():
  def observed():
    observations = []
    for count in range(5):
      print("Please enter an observation:")
      observations.append(input())
    return observations
  
  def remove_observations(observations):
    running = True
    while running == True:
      response = input("Do you wish to remove an observation (yes/no)? ")
      if response == "yes":
        observation_to_remove = input("What observation do you wish to remove? ")
        observations.remove(observation_to_remove)
        print("Done!")
      elif response == "no":
        return observations
        running == False
      else:
        print("Enter a valid answer")
  
  
  print("Counting observations...")
  observations = observed()
  remove_observations(observations)
  observations_set = set()
  
  for count in observations:
    observations_set.add((count, observations.count(count)))
    
  print("\nObservations: ")
  for count, repeats in observations_set:
    print("{} observed {} times.".format(count, repeats))
