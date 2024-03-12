class Divisor:
  def __init__(self, n):
    self.__n = n
  
  def __iter__(self):
    self.__current = 1
    return self
  
  def __next__(self):
    if self.__current <= self.__n:
      if self.__n % self.__current == 0:
        result = self.__current
        self.__current += 1
        return result
      else:
        self.__current += 1
        return self.__next__()
    else:
      raise StopIteration
