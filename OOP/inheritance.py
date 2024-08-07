class Animal:
    def eat(self):
        print("This animal is eating.")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swin(self):
        print("This fish is swimming")

rabbit = Rabbit()
fish = Fish()

rabbit.eat() #inherit
fish.sleep() #inherit
rabbit.run() #own method
fish.swim() #own method