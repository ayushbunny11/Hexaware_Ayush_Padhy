import sys
n = int(input('Enter number: '))

def squareSumMin(n):
    
    if n==0:
        return 0
    
    res = sys.maxsize
    for i in range(1, n):
        if (i*i) <= n:
            num = i*i
            count = 1 + squareSumMin(n-num)
            res = min(res, count)
        else:
            break
        
    return res  

result = squareSumMin(n)
print(f'The minimum number of squares that sum to {n} is: {result}')
