class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
class Student(Person):
  def __init__(self,fname,lname,age,height):
      super().__init__(fname,lname)
      self.age=age
      self.height=height
  def print(self):
      print(self.fname,  self.lname,  self.age,  self.height)


x = Student("Mike", "Olsen",50,'6ft')
x.print()
