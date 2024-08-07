#when a derived(child class) inherit from another child class.
#Family Tree

class Organism():
    is_alive =True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.is_alive)
dog.eat() 
dog.bark()