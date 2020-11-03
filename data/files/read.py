def run():

  def search(file_path):
    print("Searching...")
    with open(file_path) as file:
      for line in file:
        print("looked in {}".format(line))
      print("Done!")

  
  search("data/files/locations.txt")