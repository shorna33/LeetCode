def exists(i, nums):
    f = 0
    for j in range(len(nums)):
        if i == nums[j]:
            f = 1
    return f


nums = [4,3,2,7,8,2,3,1]

output = []

for i in range(len(nums)):
    index = abs(nums[i]) - 1
    nums[index] = -abs(nums[index])

for i in range(len(nums)):
    if nums[i] > 0:
        output.append(i + 1)

print(output)
