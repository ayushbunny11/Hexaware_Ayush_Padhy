# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

sen = input('Input a sentence: ')

cs=0
cd=0

for char in sen:
    if char.isdigit():
        cd+=1
    elif char.isalpha():
        cs+=1

print("Letters: ", cs)
print("Digits: ", cd)



# words = sen.split(' ')
#
# for word in words:
#     if(word.isdigit()):
#         for digit in word:
#             cd += 1
#     else:
#         for letter in word:
#             cs += 1
