#loops in python: for loops and while loops


# for i in range(5, 10): #range(start, stop, step)
#     print('Python')


# students = ['john', 'bob', 'anna', 'lise']

# for each_student in students:
#     if each_student == 'anna':
#         print('hello anna')
#     else:
#         print(each_student)

# cities = ('Tel Aviv', 'Sao Paulo', 'Moscow', 'Amsterdam')

# for city in cities:
#     print(f'I have been in {city}')

# user_num = int(input('Give me a number'))

# for i in range(1,11):
#     print(user_num * i)

#while loop
    
counter = 0
while counter < 8:
    counter += 1
    print('hello')

password = ''

while password != '12345':
    password = input('password?')
    if password == 'juliana':
        break


print('You got the right password')

current_num = 0
while current_num <= 10:
    current_num +=1
    if current_num == 5:
        continue
    else:
        print(current_num)





    