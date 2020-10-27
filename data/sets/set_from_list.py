def run():
  def observations():
    observations = []
    for count in range(7):
      print("Please enter an observation:")
      observations.append(input())
    return observations
  
  print("Counting observations...")
  observations = observations()
  observations_set = set()
  for count in observations:
    observations_set.add((count, observations.count(count)))
  print(observations_set)
