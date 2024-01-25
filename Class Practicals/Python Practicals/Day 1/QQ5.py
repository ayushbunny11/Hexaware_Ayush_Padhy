# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program
# in a comma-separated sequence.
import math

c=50
h=30
d=input('Enter the number: ')
list1 = d.split(',')
list2 = []

for i in range(len(list1)):
    q = math.sqrt((2*c*int(list1[i]))/h)
    list2.append(int(q))
print(list2)
