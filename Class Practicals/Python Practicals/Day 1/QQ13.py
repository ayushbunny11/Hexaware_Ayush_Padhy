# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sen = input('Input a sentence: ')
cu = 0
cl = 0

for char in sen:
    if char.isupper():
        cu+=1
    elif char.islower():
        cl+=1

print("Upper: ", cu)
print("Lower: ", cl)