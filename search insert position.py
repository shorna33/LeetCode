nums = [2, 3, 5, 6]
target = 11
n = len(nums)
index = 0
for i in range(n):
    if nums[i] == target:
        index = i
    elif i < n - 1:
        if (nums[i] < target) and (nums[i + 1] > target):
            index = i + 1
    elif (target > nums[i]) and (i == n-1):
        index = i + 1
    elif (target < nums[i]) and (i == 0):
        index = i
print(index)
