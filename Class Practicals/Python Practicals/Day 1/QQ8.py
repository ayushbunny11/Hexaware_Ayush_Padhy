# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines = []
while True:
    line = input()
    lines.append(line)
    if not line:
        break

for line in lines:
    print(line.upper())