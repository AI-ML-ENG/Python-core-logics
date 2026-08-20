class Person:
  def __init__(self, name, age):
    self.__name = name#private property
    self.age = age
  @property
  def get_value(self):
    return self.__name


p1 = Person("Emil", 25)
print(p1.get_value)
print(p1.age) # This will cause an error