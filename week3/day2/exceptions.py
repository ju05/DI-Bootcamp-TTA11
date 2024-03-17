# try, except blocks: avoiding to crash the program because some error.

# print('hello')) Syntax Error = specific and clear

# move = int(input('imput your move')) #Can give a ValueError if the input is not a digit
# print(move)


#how to avoid the Va
try:
    move = int(input('move: '))
    print(move)
except:
    print('invalid move')
    # move = int(input('move: '))

#TIC TAC TOW EXAMPLE
# VALID_MOVES = [i for i in range(1,10)]

while True:
    try:
        move = int(input('imput your move'))
        if move > 9:
            raise Exception('Choose a number in range 1-9')
            # raise ValueError()
        break
    except Exception as e:
        print(e) #will print: invalid literal for int() with base 10: 'w'
        continue
    finally:
        print('Thank you for the write input')


print(move)
