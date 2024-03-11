matrix_string = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''
COLUMN = 3
ROWS = 8

# matrix 2D list
# [[],[],[],[]]
rows = matrix_string.split('\n')
# print(rows)

# for i in range(len(matrix_string)):
#     sublist = list(matrix_string[i:i+COLUMN])
#     matrix.append(sublist)

# for row in rows:
#     matrix.append(list(row))

matrix = [list(row) for row in rows]

transposed_matrix = list(zip(*matrix))
print(transposed_matrix)

print(matrix)

transposed_message = [''.join(char) for char in transposed_matrix]
print(transposed_message)
dec_message = ''
final_str = dec_message.join(transposed_message)
print(final_str)

decrypted_message = ''
for char in final_str:
    if char.isalpha():
        decrypted_message += char
    else:
        decrypted_message += ' '

print(decrypted_message)

dec_message = ' '.join(decrypted_message.split())

print(dec_message)
