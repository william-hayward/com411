def run():

  def data():
    paths = {}
    style = input("What type of line (:, -- or -)? ")
    colour = input("What colour (r, g, b)? ")
    marker = input("What kind of marker (o, s or ^)? ")
    paths['style'] = style
    paths['colour'] = colour
    paths['marker'] = marker
    return paths

  def generate():
    num_of_lines = int(input("How many lines do you want to display? "))
    for count in range(num_of_lines):
      values = data()
      x = [0, rnd.randrange(1, 10)]
      y = [0, rnd.randrange(1, 10)]
      
      plt.plot(x, y, f"{values['colour']}{values['style']}{values['marker']}")
    plt.show()



  import matplotlib.pyplot as plt
  import random as rnd
  print("Running...")
  generate()
  print("Done!")
