#Inheritance logic

class Parent:
    def speak(self):
        print('Parent speaking')

class Child(Parent):
    def speak(self):
        print('Child is speaking load') 

class Grandchild(Child):
    pass

person = Parent()
person.speak()

person2 = Child()
person2.speak()

person3 = Grandchild()
person3.speak()

class Animal:

    def __init__(self, name, family, legs) -> None:
        self.name = name
        self.family = family
        self.legs = legs

    def make_sound(self):
        print(f'{self.name} is making a sounf')

class Dog(Animal):

    def __init__(self, name, family='Canidae', legs=4, trained=False):
        super().__init__(name, family, legs)
        # Animal.__init__(name, family, legs) #
        self.trained = trained

class Poodle(Dog):

    def __init__(self, name,legs, trained, cuteness, family='Canidae'):
        super().__init__(name, family, legs, trained)
        self.cuteness = cuteness


# animal1 = Animal('Toto', 'Canidae')
# animal1.make_sound()

dog = Dog('Rex')
dog.make_sound()

dog = Poodle('Rex', 4, True, 100)


# ex1

class Door:
    def __init__(self, is_opned = True) -> None:
        self.is_opened = is_opned

    def open_door(self):
        self.is_opened = True
        print('Door is opned')

    def close_door(self):
        if self.is_opened == False:
            print('Door is already closed')
        else:
            print('Door was closed')
            self.is_opened = False

class BlockedDoor(Door):
    def open_door(self):
        raise Exception('Cannot Open a Blocked Door!')

    def close_door(self):
        raise Exception('Cannot Close a Blocked Door!')


door1 = Door()
door1.close_door()

door2 = BlockedDoor()
door2.close_door()
