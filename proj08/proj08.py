str1= input("String 1:")
str2= input("String 2:")
request = input('What do you want to do:' +'\n'+'a (add indel)' + '\n' + 'd (delete)'+ '\n' + 's (score)'+ '\n' + 'q (quit)')

def compare(a, b):
    match = 0
    mismatch = 0
    if len(a)>len(b):
        i =0
        while i< len(a) - len(b):
            i+=1
            b = b + '-'
    elif len(b)>len(a):
        i = 0
        while i < len(b) - len(a):
            i +=1
            a = a +'-'
    for x, y in zip(a, b):
        if x ==y:
            match +=1
        else:
            mismatch +=1
    print('Matches: ' + str(match) + ' Mismatches: ' + str(mismatch)
          + '\n' + 'Str1: '+str1 + '\n'+ 'Str2: ' + str2 )

def add(str):
    n = int(input('Where do you want to add the indel:'))
    str = str[:n] + '-' + str[n:]
    print(str)
    return str

def delete(str):
    n = int(input('Where do you want to delete the indel:'))
    if str[n] is '-':
        str = str[:n] + str[n+1:]
        print(str)
    else:
        print('You cannot delete this')
    return str

while request is not 'q':
    if request is 's':
        res = compare(str1, str2)
    elif request is 'a':
        s = input('Which string you want to work on:')
        if s is '1':
            str1 = add(str1)
        elif s is '2':
            str2 = add(str2)
    elif request is 'd':
        s = input('Which string you want to work on:')
        if s is '1':
            str1 = delete(str1)
        elif s is '2':
            str2 = delete(str2)

    request = input(
        'What do you want to do:' + '\n' + 'a (add indel)' + '\n' + 'd (delete)' + '\n' + 's (score)' + '\n' + 'q (quit)')


