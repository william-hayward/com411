def run():
  def likelihood():
    return (50, 38, 27, 99, 4)
    
  likelihoods = likelihood()
  print("Minimum likelihood of falling: {}".format(min(likelihoods)))
  print("Maximum likelihood of falling: {}".format(max(likelihoods)))
  