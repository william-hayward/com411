def run():

  def search(file_path):
    print("Searching...")
    sections = []
    books = []
    with open(file_path) as file:
      for line in file:
        if line.startswith("Section"):
          part = line.split(":")
          sections.append(part[1][:-1])
        else:
          books.append(line[:-1])
    print("Done!")
    data = (sections, books)
    return data

  def save(file_path, data):
    print("Saving...")

    with open(file_path, "w") as file:
      file.write("Sections: ")
      for count in data[0]:
        file.write(count + ",")
      
      file.write("\nBooks: ")
      for count in data[1]:
        file.write(count + ",")
      

  data = search("data/files/books.txt")
  save("data/files/section-books.txt", data)