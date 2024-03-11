
#enumerate
cats = ['Lulu', "Miau", "chatuli"]

def make_cute():
    for i, cat_name in enumerate(cats):
        cats[i] = f'{cat_name} is cute'

    # i = 0
    # while i < len(cats):
    #     cats[i] = f'{cats[1]} is cute'
    #     i+=1
# make_cute()
# print(cats)

#list comprehension

num_list = []
for num in range(6):
    if num % 2 == 0:
        num_list.append(num)

print(num_list)

num_list2 = [num for num in range(6)]


#adding a condition
num_list2 = [num for num in range(6) if num % 2 == 0]
print(num_list2)


#dictionary comprehension

fruits = ['apple', 'banana', 'cherry', 'date']

fruits_lengths = {fruit : len(fruit) for fruit in fruits}
print(fruits_lengths)




