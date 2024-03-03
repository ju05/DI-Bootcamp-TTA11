# import this

# velue types
# str: strings
# print(type('33'))


# print('python'.capitalize())
# print('python'.upper())
# print('PYTHON'.lower())

# print('hello world python'.replace('python', 'javascript'))
# print('hello world\' python \n' * 10)

#numbers
# two types: int and float

#integers
# print(type(5))
# print(type(5.3))

# print(10 % 3)

# ex1
# my_name = 'Juliana'
# my_age = 34
# my_future_age = my_age + 123879

# print(my_future_age)
# print(my_age + 123879)

#Type casting

years_in_Israel = '14'

# years_future =  10 + int(years_in_Israel)
# print(years_future)

# my_number = 2024

# print(type(str(my_number)))

years_future =  10 + float(years_in_Israel)
# print(years_future)

# ex2
# first_name = 'Juliana'
# last_name = "Schmidt"
# print(first_name, last_name)
# print(f'My first name is {first_name}, and my last name is {last_name}')

#Booleans

# print(type(True))
#True => 1
#False => 0


# print(3 < 4)
# print('6' > '4')

# some_number = 10
# some_number == years_future
# some_number != years_future

# my_fav_number = 7

# print(some_number is not my_fav_number)

# print(bool(0))
# print(True + False)

# my_age  = 43

# my_name = "Rick"

# print(f"My name is {my_name}, and I am {my_age} years old.")
# "My name is Rick, and I am 43 years old."


# count = 0
# count += 1
# count += 1
# count += 5
# print(count)


# name = "Frank"
# print("Hello, {}. You are {}.".format(name, my_age))
# print(type(int(f'{30+4}')))

#input function

# age = int(input('what s your age?')) #the value of an input will always be a str

# count = 0
# if age == 21:
#     print('you can drink in the pub')
# elif age >= 12 and age <= 18 :
#     print('You are not allowed to come!')
# elif age > 18 or age <= 10:
#     print('You can come!yehhh')
# else: 
#     print('You can\'t come to the pub')

#ex3
user_number = int(input('Gim`me a number'))

if user_number % 3 == 0 and user_number % 5 == 0:
    print('FrizzBuzz')
elif user_number % 5 == 0:
    print('Buzz')
elif user_number % 3 == 0:
    print('Frizz')



