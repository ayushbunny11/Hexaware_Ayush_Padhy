def division_check(n):
    n= abs(n)
    
    while(n>=7):
        last_digit = n - ((n//10)*10)
        n = (n//10) - (2*last_digit)
    
    if n==0 or n==7:
        return True
    else:
        return False

n=int(input())

if(division_check(n)):
    print("Divisble")
else:
    print("NoT")