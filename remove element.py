nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
i = 0
j = 0
while (i <= j) and (j < len(nums)):
    if nums[j] == val:
        j += 1
    else:
        nums[i] = nums[j]
        i += 1
        j += 1
print(i, nums)
