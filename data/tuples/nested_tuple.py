def run():
  def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods

  likelihoods = steps()
  good_steps = []
  bad_steps = []
  for count in likelihoods:
    if count[1] < 50:
      good_steps.append(count)
    else:
      bad_steps.append(count)

  bad = len(bad_steps)
  good = len(good_steps)
  print("Good steps: {}, Bad steps: {}".format(good, bad))
 