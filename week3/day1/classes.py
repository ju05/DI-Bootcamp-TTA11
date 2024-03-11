
#  creating a class

class Dog:

    def __init__(self,name, color,age=0):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        print(f'{self.name} goes Wof!!')

    def walk(self, meters):
        print(f'{self.name} walked {meters}')
    
    # redefining attributes through a method
    def rename(self, new_name):
        self.name = new_name


# creating objects (instances)
shelter_dog = Dog('Rex', 'brown', 10)
pitbull = Dog('Fera', 'grey',6)
chowchow = Dog('Leao', 'Gingi', 4)

# accesing the internal dictionary of an object:
print(shelter_dog.__dict__)
print(type(chowchow))
print(type(pitbull))

# printing all the structure of a class in Python
# print(help(Dog))
# print(help(str))

# printing the attributes os an object (.nameofattribute)
print(shelter_dog.name)
print(pitbull.name)

# creating specific attributes for an object
chowchow.favorite_toy = 'ball'
# print(chowchow.favorite_toy)

# calling methods
pitbull.bark()
shelter_dog.bark()
chowchow.bark()
pitbull.walk(500)
shelter_dog.walk(700)
chowchow.walk(200)

# redefining attributes through a method
pitbull.rename('Flufy')
print(pitbull.name)


# data structures and objects
my_dogs = [pitbull.age, shelter_dog.age, chowchow.age] # a list of objects
# print(max(my_dogs))


# making it more reusable:
# globals().values() access all the objects created in a class
my_dogs_obj = [obj for obj in globals().values() if isinstance(obj, Dog)]


print(my_dogs_obj)
for dog in my_dogs_obj:
    older = [my_dogs_obj[0]]
    for dog in my_dogs_obj:
        if older[0].age < dog.age: 
            older[0] = dog

print(f' {older[0].name} is the oldest, {older[0].age} years old')

#______________________________ course notes exercises ________________________
# ex2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_details(self):
#         print("Hello my name is " + self.name)

#     def rename(self, newname):
#         self.name = newname



# first_person = Person("John", 36)
# first_person.show_details()
# first_person.rename('Mark')
# first_person.show_details()

# # ex3
# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()
# dell_computer.description("Mark")


# Computer.description(dell_computer, "Mark")




