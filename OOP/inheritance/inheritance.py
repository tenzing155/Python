#To inherit behaviour of one parent class to another child class
#To inherit attributes and methods of parent class by child class

# class Animal:
#     def __init__(self):
#         self.eyes = 2

#     def eat(self):
#         print("This animal is eating.")
    
#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(Animal):
#     def __init__(self):
#         super().__init__()

#     def run(self):
#         print("This rabbit is running")

# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")

# rabbit = Rabbit()
# fish = Fish()

# rabbit.eat() #inherit
# print(rabbit.eyes)
# fish.sleep() #inherit
# print(fish.eyes)
# rabbit.run() #own method
# fish.swim() #own method


# class Mobile:
#     def __init__(self, mobile_name, mobile_price, quantity):
#         self.name = mobile_name
#         self.price = mobile_price
#         self.quantity = quantity

#     def get_name(self):
#         return f"Mobile name is {self.name}"

#     def get_price(self):
#         return f"Price: {self.price}"

#     def get_quantity(self):
#         return f"Quantity: {self.quantity}"


# class Samsung(Mobile):
#     def __init__(self):
#         super().__init__("Samsung", 700, 50)


# class Xiaomi(Mobile):
#     def __init__(self):
#         super().__init__("Xiaomi", 500, 100)


# samsung = Samsung()
# xiaomi = Xiaomi()

# print(samsung.get_name())     
# print(samsung.get_price())     
# print(samsung.get_quantity())  

# print(xiaomi.get_name())       
# print(xiaomi.get_price())       
# print(xiaomi.get_quantity())    


class Mobile:
    def __init__(self, mobile_name, mobile_price, quantity):
        self.name = mobile_name
        self.price = mobile_price
        self.quantity = quantity
    
class Samsung(Mobile):
    def __init__(self,mobile_name,mobile_price,quantity):
        super().__init__(mobile_name,mobile_price,quantity)

obj = Samsung("Samsung",50000,2)
print(obj.name)
print(obj.price)
print(obj.quantity)