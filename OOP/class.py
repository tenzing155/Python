class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"My name is {self.name}, age is {self.age}.")

s1 = Student("Tenzing",21)
s1.myfunc()