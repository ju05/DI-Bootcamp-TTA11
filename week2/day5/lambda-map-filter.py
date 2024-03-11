#map

def upper_string(s):
    return s.upper()

fruits = ["Apple", "Banana", "Pear", "Orange"]

print(list(map(upper_string, fruits)))

#filter
def starts_with_A(s):
    return s[0] == "A"

print(len(tuple(filter(lambda s: s[0] == "A", fruits))))

starts_A = lambda s: print(s)

starts_A('Banana')
# my_tuple = ('Hi')
# print(type(my_tuple))
