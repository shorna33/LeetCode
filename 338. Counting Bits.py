n = 2
arr = [0 for i in range(n+1)]
nums = [0 for i in range(n+1)]
temp = 0

for i in range(n + 1):
    arr[i] = bin(i).replace("0b", "")

for i in range(n+1):
    temp = str(arr[i])
    n = len(temp)
    count = 0
    for j in range(n):
        if temp[j] == '1':
            count += 1
    nums[i] = count

print(nums)

