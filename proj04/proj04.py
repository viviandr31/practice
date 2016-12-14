import math

s = input('Please give me a square number:')
root = math.sqrt(int(s))
newstr = str(root)

if newstr[-1:] is '0':
    triangular1 = root*(root+1)/2
    triangular2 = root*(root-1)/2
    print('The original Square Number is ' + s)
    print('The tow triangular number are: ' + str(triangular1) +', ' +str(triangular2))