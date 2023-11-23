nums = [1, 2, 5, 5, 6, 6, 6, 6, 7, 9, 9]
i = 0
j = 1
while (i <= j) and (j < len(nums)):
    if nums[i] == nums[j]:
        j += 1
    else:
        nums[i+1] = nums[j]
        i += 1
print(i+1)
