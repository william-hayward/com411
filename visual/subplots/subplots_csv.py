def run():
  def read_data():
    with open("visual/subplots/temps.csv") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
      header = next(csv_reader)
      data = {
        header[0].strip():[],
        header[1].strip():[]
      }
      for row in csv_reader:
        data[header[0].strip()].append(row[0].strip())
        data[header[1].strip()].append(row[1].strip())
      return data

  import csv
  import matplotlib.pyplot as plt
  data = read_data()
  fig, (ax1, ax2) = plt.subplots(2, 1, sharex = "all")
  ax1.plot(data["week1"])
  ax2.plot(data["week2"])
  plt.tight_layout
  plt.show()