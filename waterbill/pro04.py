len = int(input('Please input the order of square:'))
top = int(input('Please input the top left number:'))

for j in range(top, len+1):
    for i in range(j, len+1):
        print(i, end='')
    for i in range(1, j):
        print(i, end='')
    print('\n')

for j in range(1, top):
    for i in range(j, len+1):
        print(i, end='')
    for i in range(1, j):
        print(i, end='')
    print('\n')

