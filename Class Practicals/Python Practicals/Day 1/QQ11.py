# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def digitEven(num):
    snum = str(num)
    for digit in snum:
        if int(digit)%2 != 0:
            return False
    return True

for i in range(1000, 3001):
    if(digitEven(i)):
        print(i, end=',')

