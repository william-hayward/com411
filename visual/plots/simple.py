def run():
  
  def display(x, y):
    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.plot(x, y)
    plt.show()

  import matplotlib.pyplot as plt
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  display(x_values, y_values)
  