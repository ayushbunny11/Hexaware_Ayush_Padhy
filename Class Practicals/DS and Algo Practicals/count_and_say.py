n = int(input('Enter the number: '))

def count_and_say(n):
    if n==1:
        return "1"
    if n==2:
        return "11"
    
    say = "11"
    
    for _ in range(2, n):
        res = ""
        count = 1
        for j in range(1, len(say)):
            if say[j] != say[j-1]:
                res = res + str(count) + say[j-1]
                count = 1
            else:
                count += 1
        
        res = res + str(count) + say[-1]
        say = res
    
    return say

print(count_and_say(n))
        