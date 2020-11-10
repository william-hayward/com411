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
      x = rnd.sample(range(1,10), num_of_lines)
      y = rnd.sample(range(1,10), num_of_lines)

      
      plt.plot(x, y, f"{values['colour']}{values['style']}{values['marker']}")
    plt.show()



  import matplotlib.pyplot as plt
  import random as rnd
  print("Running...")
  generate()
  print("Done!")
