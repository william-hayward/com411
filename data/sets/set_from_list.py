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
  for count, repeats in observations_set:
    print("{} observed {} times.".format(count, repeats))