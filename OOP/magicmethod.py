# Magic method are called without calling them.
# class Method:
#     def __del__(self):
#         print("This is destructor method") #3

#     def __init__(self):
#         print("This is constructor method") #1

#     def info(self):
#         print("This is info method") #2

# obj = Method()
# obj.info()


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"My name is {self.name}, age is {self.age}."


# s1 = Student("Tenzing",21)
# print(s1)