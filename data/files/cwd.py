def run():
  
  def cwd():
    path = os.getcwd()
    print("The current working folder is {}".format(path))
    print("The folder contains the following:")
    for count in os.listdir(path):
      print(count)
    
  import os
  print("Processing...")
  cwd()