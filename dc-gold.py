import random

# Generate list of random numbers
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

# Initialize a dictionary to hold the count of numbers
numbers_dict = {}
pair_count = 0

# Iterate over the list
for num in list_of_numbers:
    # Find the complement to the target_number
    complement = target_number - num
    
    # If the complement is already in the dictionary, a pair is found
    if complement in numbers_dict:
        pair_count += numbers_dict[complement]
    
    # If the number is already in the dictionary, increment its count, else set it to 1
    if num in numbers_dict:
        numbers_dict[num] += 1
    else:
        numbers_dict[num] = 1

# Print the count of pairs
print(pair_count)

number = bin(int(input("Enter a number: ")))
b = number[:2]
number = number[2:]
number = number[::-1]
for i in range(32-len(number)):
    number += "0"
print(int(b+number, 2))





