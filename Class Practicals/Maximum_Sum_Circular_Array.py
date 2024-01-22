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
    n = len(arr)
    if n == 0:
        return 0
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

print(f"Maximum Distance: {-1 * (total_sum - max_subarray_sum(inv_arr))}")