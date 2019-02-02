## Write a program, which find all the numbers between 100 and 500 such that each digit of the number is odd and then print the numbers.

y = 100

while y < 500:
    if ((y % 10) % 2) != 0:
        if ((y % 100) // 10) % 2 != 0:
            if (y // 100) % 2 != 0:
                print(y)
    y += 1

