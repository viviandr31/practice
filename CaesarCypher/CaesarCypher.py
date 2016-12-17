request = input('"e" to encode a string' + "\n"
                '"d" to decode a string' + "\n"
                '"q" to quit: ')
charactors = ['a','b','c','d','e','f','g','h','i', 'j', 'k','l','m','n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']

def encode(s):
    str = ''
    rotation = int(input('Give me a rotation: '))
    for c in s:
        if c in charactors:
            index = charactors.index(c)
            if index <= (25-rotation):
                str += charactors[index+rotation]
            else:
                str += charactors[index-(25-rotation)]
        else:
            str += c
    print(str)

def decode(s, a):
    for rotation in range(1, 25):
        str = ''
        for c in s:
            if c in charactors:
                index = charactors.index(c)
                if index >= rotation:
                    str += charactors[index - rotation]
                else:
                    str += charactors[index + (25 - rotation)]
            else:
                str += c
        if a in str:
            print(str)

while request is not 'q':
    if request == 'e':
        str = input('Give me a string to encode: ')
        encode(str)
    elif request == 'd':
        str = input('Give me a string to decode: ')
        a = input('Give me a word in the string')
        decode(str, a)
    elif request == 'q':
        break
    else:
        print("You input a valid request")
    request = input('"e" to encode a string' + "\n"
                    +'"d" to decode a string' + "\n"
                    +'"q" to quit: ')

print('Thanks for playing! ')