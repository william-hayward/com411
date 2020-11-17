def run():
  def read_data():
    with open("visual/subplots/titanic.csv") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
      header = next(csv_reader)
      data = {
        header[1].strip():[],
        header[4].strip():[],
        header[5].strip():[],
        header[9].strip():[]
      }
      for row in csv_reader:
        data[header[1].strip()].append(row[1].strip())
        data[header[4].strip()].append(row[4].strip())
        data[header[5].strip()].append(row[5].strip())
        data[header[9].strip()].append(round(float(row[9].strip()), 2))
      return data


  import csv
  import matplotlib.pyplot as plt
  data = read_data()
  fig, (ax1, ax2) = plt.subplots(2, 1)
  ax1.plot(data["Survived"], data["Age"])
  plt.tight_layout
  plt.show()


