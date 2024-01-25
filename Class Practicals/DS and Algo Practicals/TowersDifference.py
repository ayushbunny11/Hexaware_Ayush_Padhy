import random

n = int(input('No. of towers: '))
arr = []
print("Input Height: \n")
for i in range (n):
    arr.append(int(input()))

k = int(input('Enter K value: '))

for i in range (n):
    if random.randint(0, 1) == 0:
        arr[i] = (arr[i] - k)
    else:
        arr[i] = (arr[i] + k)

print(f'Updated Tower Heights: {arr}')

arr = sorted(arr)

print(f"Maximum difference is: {arr[-1] - arr[0]}")