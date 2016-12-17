target = input('Please enter phrase to guess: ')
target = target.lower()
maxwrong = 6
incorrect = ''
current = ''
charactors = ['a','b','c','d','e','f','g','h','i', 'j', 'k','l','m','n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']


print('Chances Remaining: ' + str(maxwrong))
print('Missed Letters/Digits: ' + incorrect)
for c in target:
    if c in charactors:
        current = current +'_'
    else:
        current = current + c
print (current)

while maxwrong >0:
    guess = input('Your guess(letters only): ')
    guess = guess.lower()
    if guess in target:
        i = 0
        for c in target:
            if c == guess:
                index = target[i:].find(c) + i
                current = current[0:index] + c + current[index+1:]
            i +=1
    else:
        if guess not in incorrect:
            incorrect= incorrect + guess
        maxwrong -=1

    if current == target:
        print('You won')
        break
    else:
        print('Chances Remaining: ' + str(maxwrong))
        print('Missed Letters/Digits: ' + incorrect)
        print(current)




if maxwrong ==0:print('You lose')



