class Animal:
    def make_sound(self):
        return "Some generic sound"


class Mammal(Animal):
    def give_birth(self):
        return "Live birth"


class Bird(Animal):
    def lay_eggs(self):
        return "Lay eggs"


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"


class Parrot(Mammal):
    def make_sound(self):
        return "Echolocation!"









print("MRO for Animal:", Animal.__mro__)
print("MRO for Mammal:", Mammal.__mro__)
print("MRO for Bird:", Bird.__mro__)
print("MRO for Dog:", Dog.__mro__)
print("MRO for Parrot:", Parrot.__mro__)


dog = Dog()
bird = Bird()
parrot = Parrot()


print("Dog says:", dog.make_sound())  
print("Bird says:", bird.make_sound())  
print("Parrot says:", parrot.make_sound())  
