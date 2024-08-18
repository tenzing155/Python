# class are blue print of object
# object are instance of class

# class Student:
#     name = "Tenzing"
#     age = 21

#     def address(self,name):
#         print(f"{name}")

# instance of class
# student = Student()
# print(student.name)
# print(student.age)
# student.address("kapan")

# class Student:
    # def __init__(self,name,age,address):
    #     self.name = name
    #     self.age = age
    #     self.address = address

#     def info(self):
#         print(f"My name is {self.name}, age is {self.age} and address is {self.address}")

# std = Student("Tenzing",21,"kapan")
# std.info()


# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def details(self):
#         print(f"Name is {self.name}, age is {self.age} and salary is {self.salary}")

# employee = Employee("Hari",34,50000)
# employee.details()


# class Calculator:
#     def add(self,a,b):
#         return a + b

#     def sub(self,a,b):
#         return a - b
    
#     def mul(self,a,b):
#         return a * b
    
#     def div(self,a,b):
#         return a / b
    
#     def mod(self,a,b):
#         return a % b

#     def floor(self,a,b):
#         return a // b
    
#     def expo(self,a,b):
#         return a ** b
    
# calc = Calculator()

# print(f"Addition is {calc.add(2,2)}")
# print(f"Subtraction is {calc.sub(10,2)}")
# print(f"Multiplication is {calc.mul(2,2)}")
# print(f"Division is {calc.div(10,2)}")
# print(f"Modulus is {calc.mod(50,4)}")
# print(f"Floor division is {calc.floor(10,3)}")
# print(f"Exponentiation is {calc.expo(2,4)}")


# class Product:
#     product_list = [
#         {'name' : 'apple', 'price' : 100},
#         {'name' : 'banana', 'price' : 50},
#         {'name' : 'orange', 'price' : 150}
#     ]

#     def show_product(self):
#         for product in Product.product_list:
#             print(product)

    
#     def add_product(self,name,price):
#         new_product = {'name' : name, 'price': price}
#         Product.product_list.append(new_product)
        
#     def delete_product(self,name):
#         for product in Product.product_list:
#             if product["name"] == name:
#                 Product.product_list.remove(product)

#     def update_product(self,name,new_name,new_price):
#         for product in Product.product_list:
#             if product["name"] == name:
#                 product["name"] = new_name
#                 product["price"] = new_price
#                 break


# product = Product()

# product.show_product()

# product.add_product('strawberry',160)
# product.show_product()

# product.delete_product('strawberry')
# product.show_product()

# product.update_product('apple','green_apple',130)
# product.show_product()



# class Shape:
#     def __init__(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         area_of_rectangle = self.length * self.breadth
#         print(f"Area of rectangle is {area_of_rectangle}")


# class Circle(Shape):
#     def __init__(self, radius, pie=3.14):
#         self.radius = radius
#         self.pie = pie

#     def area(self):
#         area_of_circle = self.pie * self.radius * self.radius
#         print(f"Area of circle is {area_of_circle}")


# rectangle = Rectangle(12, 6)
# rectangle.area()


# circle = Circle(7)
# circle.area()



# class Fruit:
#     def __init__(self,color,price):
#         self.color = color
#         self.price = price

#     def call(self,fruit):
#         print(f"Fruit: Color={fruit.color}, Price={fruit.price}")


# class Apple(Fruit):
#     def __init__(self,color,price):
#         super().__init__(color,price)
    
        
#     def call(self):
#         self.has_branch = 1
#         print(f"Apple: Color={apple.color}, Price={apple.price}, has branch = {self.has_branch}")


# class Orange(Fruit):
#     def __init__(self,color="orange",price=100):
#         super().__init__(color,price)

#     def call(self):
#         self.has_branch = 0
#         print(f"Orange: Color={orange.color}, Price={orange.price}, has branch = {self.has_branch}")


# apple = Apple("Red",120)
# orange = Orange()

# apple.call()
# orange.call()


