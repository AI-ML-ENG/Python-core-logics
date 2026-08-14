class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"hello{self.name} your age is {self.age}"
person1=Person("MOEEZ",26)
a=person1.greet()
print(a)
print(person1.age(7))
print(person1)