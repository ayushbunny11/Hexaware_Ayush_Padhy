n = int(input('No. of elements: '))
arr = []
print("Input: \n")
for i in range (n):
    arr.append(int(input()))

total_sum = 0   
for i in range(n):
    total_sum += arr[i]

inv_arr = []
for i in range(n):
    inv_arr.append(arr[i]*-1)

def max_subarray_sum(arr):
    maxi=float('-inf')
    sum = 0
    for i in range(n):
        sum = sum+arr[i]
        if(sum>maxi):
            maxi = sum
        if(sum<0):
            sum = 0
    return maxi
    
print(max_subarray_sum(inv_arr))
print(f"Maximum Distance: {-1 * (total_sum - max_subarray_sum(inv_arr))}")