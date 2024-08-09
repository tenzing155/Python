class Animal:
    def __init__(self):
        self.eyes = 2

    def eat(self):
        print("This animal is eating.")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def __init__(self):
        super().__init__()

    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

rabbit = Rabbit()
fish = Fish()

rabbit.eat() #inherit
print(rabbit.eyes)
fish.sleep() #inherit
rabbit.run() #own method
fish.swim() #own method