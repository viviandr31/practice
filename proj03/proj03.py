s = input('Input a large whole number:')
n = input('Input the split (whole number): ')
temp =''
substring=[]
i = 0

for c in s:
   temp += c
   if (len(temp) == int(n)):
       substring.append(temp)
       temp =''

print(substring)

increasing = True
for i in range(1, len(substring)):
    if substring[i] < substring[i-1]:
        increasing = False
        break

print(increasing)
