user_name = 'John'
user_email = 'john@gmail.com'
user_age = 25

user_info = [user_name, user_email, user_age]
print(user_info[1])

#how to create a list
user_name_list = [user_name]
# print(user_name_list)

user_name_list2 = list(user_name)
# print(user_name_list2)

user_name_list3 = user_name.split()
# print(user_name_list3)

# user_info2 = input('Give me your name, email and age separated by ,: ').split(',')

# print(user_info2)

# lists methods

# adding element
# user_info2.append('betzalel')
# print(user_info2)
# print(user_info2[-2])


fav_color_list = ['red', 'blue', 'yellow', 'green', 'pink', 'blue']

#changing an element
fav_color_list[1] = 'green'
# fav_color_list[0] = fav_color_list[1]
# fav_color_list[0] = fav_color_list[1]
# print(fav_color_list)

# sorting methods
# sort() and sorted()
# fav_color_list.sort() #sorts the original
# print(fav_color_list)

# new_list = sorted(fav_color_list)
# print('original: ',fav_color_list)
# print(new_list)

# #removing element
# fav_color_list.remove('yellow')
# print(fav_color_list)

fav_color_list.pop() #no arguments will remove the last element
# print(fav_color_list)

fav_color_list.pop(2)
# print(fav_color_list)

#finding element index
# print(fav_color_list.index('pink'))

# EXERCISE
# Given this list:
list1 = [5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# Hint : Look at the index method

#option1
# list1[list1.index(20)] = 200
# print(list1)

print(max(list1))
print(min(list1))
print(sum(list1))

#tuples: sequence that can't be change
# some_tuple = (1,2,3,4)

# print(some_tuple[2])
# some_tuple[2] = 15
# fav_colors_tuple = tuple(fav_color_list)
# print(some_tuple)
# print(fav_colors_tuple)

# a,b,c,d = (10,20,30,40)
# print(a)
# print(b)
# print(c)
# print(d)

#sets: is a collection that is unordered and has no duplicates
clean_set = set(fav_color_list)
set2 = {'john', 'lise', 'daniel'}
# print(clean_set)

# clean_set.add('purple')
# clean_set.add('grey')
# clean_set.add('purple')
# print(clean_set)

words = ['hello', 'there', 'python']
shuffled_words = set(words)
# print(shuffled_words)

joined_sets = clean_set.union(set2)


joined_sets.remove('yellow')
print(joined_sets)

joined_sets.pop()




