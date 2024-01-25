n = int(input('No. of elements: '))
arr = []
print("Input: \n")
for i in range (n):
    arr.append(int(input()))

res = [1]*n

def productReplace(arr: list):
    left = 1
    right = 1
    for i in range(1, n):
        left = left * arr[i-1]
        res[i] = res[i] * left

    for i in range(n-2, -1, -1):
        right = right * arr[i+1]
        res[i] = res[i] * right

    return res

print(productReplace(arr))
    