def openfile():
    file = open('measles.txt')
    return file

def processfile(file):
    year = input("Enter a year:")
    income = input('Income lever:')
    min =100
    max =0
    sum =0
    total =0
    if income is '1':
        income = 'WB_LI'
    elif income is '2':
        income = 'WB_LMI'
    elif income is '3':
        income = 'WB_UMI'
    else:
        income = 'WB_HI'
    str = file.read();
    for item in str.split("\n"):
      if income in item and year in item:
            a = item.split(' ')
            arr = []
            for s in a:
                if s is not '':
                    arr.append(s)
            print(arr)
            sum +=int(arr[2])
            if int(arr[2])<min: min = int(arr[2])
            if int(arr[2])>max: max = int(arr[2])
            total +=1
    print(min, max, sum/total)


file = openfile()
processfile(file)