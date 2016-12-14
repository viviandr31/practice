fo = open("measles.txt")
str = fo.read();
year = input("Select the year:")
filename = input("File name:")
filename = filename + '.txt'
outputfile = open(filename, "w")
for item in str.split("\n"):
    if year in item:
        outputfile.write(item + '\n')
        print(item)
    elif year in ['', 'all', "ALL"]:
        outputfile.write(str)


