nums = [3, 1, 2, 10, 1]

n = len(nums)
result = []
for x in range(n):
    sum = 0
    for y in range(x+1):
        sum = sum + nums[y]
    result.append(sum)
print(result)
