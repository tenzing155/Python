#abstract class(abstraction) - showing only necessary data/features and hiding the unnecessary complex data 
#parent class which is incomplete or not made fully
#child class should inherit all abstract methods of the parentclass/Abstract class 
# we need to import abc,ABC and abstract methods to use abstract class

# from abc import ABC, abstractmethod

# class Vechile(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vechile):
#     def go(self):
#         print("Car moved")

#     def stop(self):
#         print("Car stopped")


# class Bike(Vechile):
#     def go(self):
#         print("Bike moved")         #inherit all abstract methods if not it will throw error 

#     def stop(self):
#         print("Bike stopped")


# car = Car()
# bike = Bike()

# car.go()
# bike.stop()