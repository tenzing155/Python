#Having many forms 
# from abc import ABC, abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):
#         return "Area of Shape"

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         return self.side ** 2
    
# class Pizza(Circle):
#     def __init__(self,kind,radius):
#         super().__init__(radius)
#         self.kind = kind
#         self.radius = radius


# shapes = [Circle(2),Square(4),Pizza("Pepporoni",8)]

# for shape in shapes:
#     print(f"Area is {shape.area()}")