filename = input("Input file name: ")
infile = open(filename, 'r')
line = infile.readline()

letters = 0
words = 1

while line != "":
    for letter in line:
        if letter != " ":
            letters += 1
            print(letter, end = '')
        if letter == " ":
            print(end= " ")
            words += 1
    print("Letters :", letters, end = " ")
    print ("Words :", words, end = " ")
    print(" ")
    letters = -1
    words = 1
    line = infile.readline()
