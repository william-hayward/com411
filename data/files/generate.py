def run():
  def search(file_path):
    print("Searching...")
    data = {}
    with open(file_path) as file:
      section_name = ""
      for line in file:
        if line.startswith("Section"):
          part = line.split(":")
          section_name = part[1].strip()
        else:
          if section_name in data:
            values = data[section_name]
            values.append(line.strip())
          else:
            data[section_name] = [line.strip()]
    print("Done!")
    return data

  data = search("data/files/books2.txt")
  with open ("data/files/generated.csv", "w") as file:
    for count in data.items():
      section = count[0]
      books = count[1]
      for book in books:
        file.write(f"{section},{book}\n")



