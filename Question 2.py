## imagine that you have a list contains string of:list=["1", "4", "0", "6", "9"]how can you sort out this list such that the result will be [0,1,4,6,9]
x, y, z = 0, 0, 0
numList = ["1", "4", "0", "6", "9"]

for x in range(len(numList)):
    for z in range(len(numList) - 1):
        if numList[z] > numList[z+1]: ## If element "x" is bigger than the element immediately after it, swap places.
            y = numList[z+1]
            numList[z+1] = numList[z]
            numList[z] = y
        y = 0

print(numList)

