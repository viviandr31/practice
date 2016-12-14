def validate(str):
    if str.isdigit():
        if len(str) is not 5:
            str = input('Administrator inputed a number not 5 digit, please input a 5 digit number:')
            validate(str)
        else:
            for c in str:
              if str.count(c) > 1:
                str=input('Administrator inputed a repeat number. Input again: ')
                validate(str)
    else:
        str= input('Administrator inputed a nonvalid number. Input again: ')
        validate(str)
    print('\n' + '\n' +
          '\n')
    return str

def validateguess(str):
    if str.isdigit():
        if len(str) is not 5:
            str = input('Player inputed a number not 5 digit, please input a 5 digit number:')
            validateguess(str)
    else:
        str = input('Player inputed a nonvalid number. Input again: ')
        validateguess(str)
    return str



maxguess = 10
target = input('Administrator give a number:')
target = validate(target)
guess = input('Player guess: ')
guess = validateguess(guess)


