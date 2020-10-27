def run():
  def observed():
    observations = []
    for count in range(5):
      print("Please enter an observation:")
      observations.append(input())
    return observations
  
  def remove_observations(observations):
    while running == True:
      response = input("Do you wish to remove an observation (yes/no)? ")
      if response == "yes":
        observation_to_remove = input("What observation do you wish to remove? ")
        observations_set.discard(observation_to_remove)
        print("Done!")
      elif response == "no":
        return observations_set
        running == False
      else:
        print("Enter a valid answer")
  
  running = True
  print("Counting observations...")
  observations = observed()
  observations_set = set()
  
  for count in observations:
    observations_set.add((count, observations.count(count)))
  
  remove_observations(observations)
  print("\nObservations: ")
  print(observations_set)
