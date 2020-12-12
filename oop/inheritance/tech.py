from abc import ABC, abstractmethod

class Tech(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def activate(self):
    pass

  @abstractmethod
  def deactivate(self): 
    pass