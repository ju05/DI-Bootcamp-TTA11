class Alien:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        print(self.name, 'is flying!')

    def sleep(self):
        print("Aliens don't sleep")

class Animal:
    def __init__(self, name):
        self.name = name

    # def sleep(self):
    #     print("zzzZZZZZ")

class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))

    # def sleep(self):
    #     print("sleeeeeeeping")

class AlienDog(Dog, Alien):
    def __init__(self, name,planet):  # Assuming a default planet
        Dog.__init__(name)  # Calls the __init__ method of Dog
        Alien.__init__(self, name, planet)  # Calls the __init__ method of Alien
    # def __init__(self, name,planet, spacebarc):
    #     super().__init__(name, planet)
    #     self.spacebarc = spacebarc

alien_dog = AlienDog('Rex', 'Jupiter')
print(alien_dog.planet)
alien_dog.sleep()