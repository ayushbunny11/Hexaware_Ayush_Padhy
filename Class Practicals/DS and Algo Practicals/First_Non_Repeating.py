n = int(input('No. of elements: '))
arr = []
print("Input: \n")
for i in range (n):
    arr.append(int(input()))
    
for i in range(n):
    res = False
    for j in range(n):
        if i!=j and arr[i] == arr[j]:
            res = True
            break
    if(res == False):
        print(f"FNR element : {arr[i]}")
        break