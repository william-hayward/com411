def run():
  def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods
  
  likelihood_value = likelihood()
  print("Minimum likelihood of failing: {}".format(min(likelihood_value)))