#when a child class is derived form more than one parent class

class Hernivorous():
    def grass(self):
        print("This animal eats grass")

class Carnivorous():
    def meat(self):
        print("This animal eats meat")

class Omnivorous(Hernivorous,Carnivorous):
    def both(self):
        print("This animal eats both meat and grass.")


lion = Carnivorous()
lion.meat()

cow = Hernivorous()
cow.grass()

human = Omnivorous() #multiple inherit
human.both()
