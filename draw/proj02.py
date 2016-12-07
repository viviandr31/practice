nickel = 5
dime = 10
quarter = 25
deposit = 0

number_nickel = 25
number_dime = 25
number_quarter = 25
number_one = 0
number_five = 0

print("Welcome to the vending machine change maker program" +'\n' +
      'Change maker initialized' +'\n' + 'Stock contains:' +
       '\n' + str(number_nickel) + '  nickels' + '\n' + str(number_dime) + ' dimes' +
       '\n' + str(number_quarter) + ' quarters')

price = input('Enter the purchase price(XX.XX) or "q" to quit:')

def checkprice(a):
    p = float(a)
    while ( round(p*100) % 5!= 0):
        print('Illegal price: Must be a non-negative multiple of 5 cents')
        p = float(input('Enter the purchase price(XX.XX) or "q" to quit:'))
    return p

def menu():
    print("Menu for Deposits:" + '\n' + "'n' - deposit a nickel"
          + '\n' + "'d'- deposit a dime"
          + '\n' + "'q'- deposite a quarter"
          + '\n' + "'o'- deposite a one dollar bill"
          + '\n' + "'f'- deposite a five dollar bill"
          + '\n' + "'c'- cancel the purchase")



if(price !='q'):
    price = checkprice(price)
    menu()
    remain = price - deposit
    while(remain >0):
        print("Payment due:" + str(round(remain*100)/100))
        temp = input('Indicate your deposit:')
        if (temp == 'n'):
            number_nickel += 1
            deposit = 0.05
        if (temp == 'd'):
            number_dime += 1
            deposit = 0.10
        if (temp == 'q'):
            number_quarter += 1
            deposit = 0.25
        if (temp == 'o'):
            number_one += 1
            deposit = 1
        if (temp == 'f'):
            number_five += 1
            deposit = 5
        remain = remain - deposit

    print("Please take the change below" + str(round(remain*100)/100))

# remain = round(remain*100)
# if(remain/25 < -1):

res = {
    '0.25': 0,
    '0.1': 0,
    '0.05': 0,
}

remaining_amount = {
    '0.25': 1,
    '0.1': 2,
    '0.05': 3,
}

remain = -remain
for quan in [0.25, 0.1, 0.05]:
    (a, b) = divmod(remain, quan)
    real_a = remaining_amount[str(quan)] if a > remaining_amount[str(quan)] else a
    res[str(quan)] = real_a
    remain -= real_a * quan
    if b == 0: break

print(res)
print(remain)
