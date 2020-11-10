def run():

  def coordinate():
    x = int(input("Please enter an x value: "))
    y = int(input("Please enter a y value: "))
    return (x, y)

  def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for count in range(4):
      data = coordinate()
      x_values.append(data[0])
      y_values.append(data[1])
    return [x_values, y_values]


  import matplotlib.pyplot as plt
  values = path()
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.plot(values[0], values[1], 'ro--')
  plt.show()