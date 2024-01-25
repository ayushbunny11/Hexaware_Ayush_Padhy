# Find the maximum difference between two array elements that satisfies the given constraints
# Given an integer array, find the maximum difference between two elements 
# in it such that the smaller element appears before the larger element.
# For example:Input:  { 2, 7, 9, 5, 1, 3, 5 } Output: The maximum difference is 7. The pair is (2, 9)

n = int(input('No. of elements: '))
arr = []
print("Input: \n")
for i in range (n):
    arr.append(int(input()))

max = 0
pair = (0, 0)

for i in range(n):
    for j in range(i+1, n):
        if(abs((arr[i]-arr[j])) >= max):
            if(arr[i]<arr[j]):
                max = abs((arr[i]-arr[j]))
                pair = (arr[i], arr[j])
            

if(max == 0):
    print("No such pair found")
else:
    print(max, pair)
    

