s = 'y'

while(s is 'y'):
    var1, var2 = [int(x) for x in input("Enter two numbers here: ").split()]
    res =0
    print( "A = " + str(var1) + ' and B = ' + str(var2) )

    if(var2>0):
        while(var2 >= 1):
            if(var2%2 is 1):
                res += var1
                print('B was odd, we add A to make the product:' + str(res))
            var1 = var1*2
            var2  = var2//2
            if(var2>0):
                print("A = " + str(var1) + ' and B = ' + str(var2))
        s=input('Do you want to continue?(y/n):')
    elif(var1<0 and var2<0):
        var1= -var1
        var2= -var2
        while (var2 >= 1):
            if (var2 % 2 is 1):
                res += var1
                print('B was odd, we add A to make the product:' + str(res))
            var1 = var1 * 2
            var2 = var2 // 2
            if (var2 > 0):
                print("A = -" + str(var1) + ' and B = -' + str(var2))
        s = input('Do you want to continue?(y/n):')
    else:
        var2= -var2
        while (var2 >= 1):
            if (var2 % 2 is 1):
                res += var1
                print('B was odd, we add A to make the product: -' + str(res))
            var1 = var1 * 2
            var2 = var2 // 2
            if (var2 > 0):
                print("A = " + str(var1) + ' and B = -' + str(var2))
        s = input('Do you want to continue?(y/n):')