def run():

  def read_data(file_path):
    with open(file_path) as file:
      temperatures = []
      for line in file:
        temp = float(line.strip())
        temperatures.append(temp)
      return temperatures

  import matplotlib.pyplot as plt
  data = read_data("visual/subplots/temps.txt")

  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(1, 8), data)
  ax2.bar(range(1, 8), data)
  plt.tight_layout
  plt.show()



  