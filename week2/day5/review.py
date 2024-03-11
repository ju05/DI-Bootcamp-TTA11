#Basic Value Types

#Strings
#Integers: whole numbers
#floats: decimal
#Booleans: True = 1 or False = 0

greeting = 'Hello, welcome!' #string
age = 35 #integer
height = 1.80 #floats
is_female = True #boolean

#strings are sequence of characters
#acessing character by index:
print(greeting[0])
print(greeting[4])

#slicing strings
print(greeting[7:])
print(greeting[:5])

#Data structures
#1- Sequences
#Lists: ordered and mutable
#Tuples: ordered unmutable
#2 - Collections
#Sets
#Dictionaries

#lists
# students1 = list('Harry', "Hermione", 'Ron')
students = ['Harry', "Hermione", 'Ron']

#accessing list elements
# print(students[-1])
# print(students[2])
# print(students[-2])
# print(students[1])

#list methods:
#append
# students.append('Luna')
# print(students)

# students.clear()
# print(students)

# students.insert(2, 'Malfoy')
# print(students)

# students.pop(1)
# print(students)

#tuples: ordered
my_tuple = tuple()
my_tuple = (10, 20, 30, 40, 50)
my_str_tuple = ('ZA', 'Aaa', 'A')

# print(my_tuple[2])

#unpacking tuples
country, capital, population = ('Brazil', 'Brasilia', 21400000)
# print(country)
# print(capital)
# print(population)

my_tuple1 = (15, 25)
# tuple3 = my_tuple + my_tuple1
# print(tuple3)

#build-in functions for lists and tuples
# print(max(my_str_tuple))
# print(min(my_tuple))
# print(sum(my_tuple))

#Sets: unordered dont accept duplicates 
set1 = {1, 2, 3, 4, "hi", "world", "python"}
print('python' in set1)
set1.remove('world')
print(set1)

#checking similarity or difference between sets
a = {1, 2, 3, 4, 5, 5}
b = {2, 3, 6, 7, 5}
c = {10, 3, 12, 7, 5,1}
# print(a^b^c)
# print((a-b) - c)
# print(b-a)

print(a)

#dictionaries: unordered, mutable
user_a = {
    'first_name': 'Bob',
    'last_name': 'Ross',
    'age': 53,
    'address': 'Tel Aviv',
    'family': [('Jessica', 34), ('Tommy', 8)]
}

#accessing dict value

print(user_a['address'])
print(user_a['family'][1][0])

print(user_a.keys())
# looping through the keys

for key in user_a.keys():
    print(key)

for value in user_a.values():
    print(value)

for key, value in user_a.items():
    print(key, value)

#adding entries (key:value) in dicts
#option1
user_a['profession'] = 'driver'

#option2

dict_to_add = {'profession': 'driver',
               'ID': 33339993,
               'car_brand':'citroen'}
user_a.update(dict_to_add)
print(user_a)




