def sum(digit_str):
    sum_times = 0
    print('Additive loop:')
    while (len(digit_str) > 1):
        t = 0
        for c in digit_str:
            t += int(c)
        digit_str = str(t)
        print('sum =' + digit_str)
        sum_times += 1
    return (digit_str, sum_times)


def mul(b):
    mp = 0
    print('Multiplicative loop:')
    while (len(b) > 1):
        m = 1
        for c in b:
            m *= int(c)
        b = str(m)
        print('product:' + b)
        mp += 1
    return (b, mp)


"""main loop"""
s = input('Please give me an integer(negative integer to quit:')
while(int(s)>0):
    if(int(s)>0):
        ar,ap = mul(s)
        mr,mp = sum(s)
        print(ar, ap)
        print(mr, mp)

    s = input('Please give me an integer(negative integer to quit:')