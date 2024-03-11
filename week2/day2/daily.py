user_word = "ttiiitllleee"


result = [] #result = ['p']

for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        result.append(user_word[i])
    else:
        continue

print(''.join(result))

