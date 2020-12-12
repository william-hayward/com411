from clothing_size import ClothingSize
class Clothing:
  def __init__(self, colour, material, size):
    self.colour = ""
    self.material = ""
    self.size = size
  
  def check_size(clothing):
    if clothing == ClothingSize.x_small:
      pass
    elif clothing == ClothingSize.small:
      pass
    elif clothing == ClothingSize.medium:
      pass
    elif clothing == ClothingSize.large:
      pass
    elif clothing == Clothing.x_large:
      pass

if (__name__ == "__main__"):
  red_silk = Clothing("Red", "Silk", ClothingSize.medium)
  print(red_silk)