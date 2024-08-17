#same method but method is override of its parent class
class Animal():
    def eat(self):
        print("Animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating")

rabbit = Rabbit()
rabbit.eat()