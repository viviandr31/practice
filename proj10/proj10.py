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



maxguess = 3
target = input('Administrator give a number:')
target = validate(target)


guesstime = 0

while maxguess > guesstime:
    match = 0
    position = 0
    guess = input('Player guess: ')
    guess = validateguess(guess)
    for dig in guess:
        if dig in target:
            match +=1
    for x, y in zip(target, guess):
        if x ==y:
            position +=1
    print('The number of correct digit is ' + str(match) +'\n' + 'The number in the correct position as ' + str(position))
    guesstime +=1
    if position == 5:
        print('You guessed ' + str(guesstime) + " times to make it")
        break
    s = input('Do you want to quit? q for quit: ')
    if s is 'q':
        print("You lost. You have guessed " + str(guesstime) + " times")
        break

if guesstime == maxguess:
    print('You lost')



